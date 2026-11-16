import uuid
import datetime
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db, AsyncSessionLocal
from backend.app.models.user import User
from backend.app.models.preference import UserPreference
from backend.app.models.search import SearchSession, ShoppingRequest
from backend.app.models.product import Product
from backend.app.models.recommendation import Recommendation
from backend.app.models.agent_log import AgentTask, AuditLog
from backend.app.schemas.search import SearchQueryRequest, SearchSessionResponse
from backend.app.security.dependencies import get_current_user
from backend.app.services.stream_manager import stream_manager
from agents.orchestrator.agent import orchestrator_agent

router = APIRouter(prefix="/search", tags=["AI Shopping Search"])


@router.post("/query")
async def execute_search(
    req: SearchQueryRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    session_id = req.session_id or str(uuid.uuid4())
    
    # 1. Fetch user memory / preferences for personalization
    pref_stmt = select(UserPreference).where(UserPreference.user_id == current_user.id)
    pref_res = await db.execute(pref_stmt)
    pref = pref_res.scalar_one_or_none()
    user_prefs_dict = {}
    if pref:
        user_prefs_dict = {
            "preferred_brands": pref.preferred_brands or [],
            "budget_max": pref.budget_max,
            "preferred_ram": pref.preferred_ram,
            "preferred_storage": pref.preferred_storage,
            "avoid_refurbished": pref.avoid_refurbished,
            "excluded_keywords": pref.excluded_keywords or []
        }

    # 2. Persist SearchSession
    session_title = req.query[:50] + ("..." if len(req.query) > 50 else "")
    search_session = SearchSession(
        id=session_id,
        user_id=current_user.id,
        title=session_title,
        status="running"
    )
    db.add(search_session)

    shopping_req = ShoppingRequest(
        id=str(uuid.uuid4()),
        session_id=session_id,
        raw_query=req.query,
        budget_max=req.custom_budget_max,
        status="in_progress"
    )
    db.add(shopping_req)
    await db.commit()

    # Callback to stream events to WebSocket / SSE subscribers
    step_counter = 0
    async def on_stream_event(agent_name: str, status: str, message: str, payload: any):
        nonlocal step_counter
        step_counter += 1
        event_dict = {
            "session_id": session_id,
            "agent_name": agent_name,
            "status": status,
            "message": message,
            "step_index": step_counter,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "payload": payload
        }
        await stream_manager.broadcast_event(session_id, event_dict)

    # 3. Execute Multi-Agent Workflow
    workflow_result = await orchestrator_agent.execute_workflow(
        query=req.query,
        user_preferences=user_prefs_dict,
        custom_budget_max=req.custom_budget_max,
        on_event=on_stream_event
    )

    # 4. Save results in DB
    plan = workflow_result.get("plan", {})
    shopping_req.category = plan.get("category")
    shopping_req.budget_max = plan.get("budget_max")
    shopping_req.required_features = plan.get("required_features", [])
    shopping_req.preferred_features = plan.get("preferred_features", [])
    shopping_req.optional_features = plan.get("optional_features", [])
    shopping_req.excluded_features = plan.get("excluded_features", [])
    shopping_req.status = "completed"
    search_session.status = "completed"

    # Save recommendations
    db_products_stmt = select(Product)
    db_products_res = await db.execute(db_products_stmt)
    existing_products = {p.name.lower(): p for p in db_products_res.scalars().all()}

    saved_recs = []
    for rp in workflow_result.get("ranked_products", []):
        # Match with DB product if exists, or insert new live product
        matched_db_prod = None
        for ep_name, ep in existing_products.items():
            if ep.name.lower() in rp.get("name", "").lower() or (ep.brand and ep.brand.lower() == rp.get("brand", "").lower() and ep.model and ep.model.lower() in rp.get("name", "").lower()):
                matched_db_prod = ep
                break
        
        prod_id = matched_db_prod.id if matched_db_prod else None
        if not prod_id:
            # Dynamically persist live web product
            from backend.app.models.product import ProductSpec
            from backend.app.models.price import ProductPrice, Seller
            
            new_prod_id = "prod_" + str(uuid.uuid4()).replace("-", "")[:12]
            rp_specs = rp.get("specifications", {})
            new_prod = Product(
                id=new_prod_id,
                name=rp.get("name", "Live Discovered Product"),
                brand=rp.get("brand", "Verified Brand"),
                model=rp.get("model", ""),
                category=plan.get("category", "laptop"),
                description=rp.get("recommendation_explanation", ""),
                main_image=rp.get("image_url") or rp.get("image"),
                product_url=rp.get("product_url") or rp.get("url"),
                source=rp.get("source", "Live Authorized Web Store"),
                rating=rp.get("rating", 4.3),
                review_count=rp.get("review_count", 150),
                trust_score=rp.get("trust_score", 1.0),
                is_verified=True
            )
            db.add(new_prod)
            await db.flush()

            spec_obj = ProductSpec(
                product_id=new_prod.id,
                ram_gb=rp_specs.get("ram_gb", 16),
                storage_gb=rp_specs.get("storage_gb", 512),
                cpu=rp_specs.get("cpu"),
                gpu=rp_specs.get("gpu"),
                screen_size_inches=rp_specs.get("screen_size_inches", 15.6),
                battery_life_hours=rp_specs.get("battery_life_hours", 7.0),
                warranty_months=rp_specs.get("warranty_months", 12),
                raw_specs=rp_specs
            )
            db.add(spec_obj)

            seller_name = rp.get("seller") or rp.get("source") or "Authorized Merchant"
            sel_stmt = select(Seller).where(Seller.name == seller_name)
            sel_res = await db.execute(sel_stmt)
            sel_obj = sel_res.scalar_one_or_none()
            if not sel_obj:
                sel_obj = Seller(
                    id="sel_" + str(uuid.uuid4()).replace("-", "")[:8],
                    name=seller_name,
                    platform=seller_name.split()[0],
                    rating=4.5,
                    is_verified=True
                )
                db.add(sel_obj)
                await db.flush()

            price_val = float(rp.get("price", 0.0))
            orig_val = float(rp.get("original_price", price_val))
            discount = round(((orig_val - price_val) / orig_val) * 100, 1) if orig_val > price_val else 0.0
            price_obj = ProductPrice(
                product_id=new_prod.id,
                seller_id=sel_obj.id,
                current_price=price_val,
                original_price=orig_val,
                discount_percentage=discount,
                currency="INR",
                availability=rp.get("availability", "In Stock"),
                shipping_cost=0.0
            )
            db.add(price_obj)
            prod_id = new_prod.id
            rp["id"] = prod_id

        rec = Recommendation(
            request_id=shopping_req.id,
            product_id=prod_id,
            score_overall=rp.get("score_overall", 80.0),
            score_match=rp.get("score_match", 80.0),
            score_price=rp.get("score_price", 80.0),
            score_performance=rp.get("score_performance", 80.0),
            score_reviews=rp.get("score_reviews", 80.0),
            badge=rp.get("badge"),
            budget_status=rp.get("budget_status", "Within Budget"),
            explanation=rp.get("recommendation_explanation", "Matches user requirements."),
            breakdown={"specifications": rp.get("specifications", {})}
        )
        db.add(rec)
        saved_recs.append(rec)

    # Audit log
    audit = AuditLog(
        user_id=current_user.id,
        action="SEARCH_COMPLETED",
        resource_type="SearchSession",
        resource_id=session_id,
        details={"query": req.query, "category": plan.get("category")}
    )
    db.add(audit)
    await db.commit()

    return {
        "session_id": session_id,
        "request_id": shopping_req.id,
        "query": req.query,
        "plan": plan,
        "ranked_products": workflow_result.get("ranked_products", []),
        "flagged_products": workflow_result.get("flagged_products", []),
        "comparison_matrix": workflow_result.get("comparison_matrix", []),
        "comparison_highlights": workflow_result.get("comparison_highlights", {}),
        "rag_insight": workflow_result.get("rag_insight", {})
    }


@router.get("/history")
async def get_search_history(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(SearchSession)
        .where(SearchSession.user_id == current_user.id)
        .order_by(SearchSession.created_at.desc())
        .limit(30)
    )
    res = await db.execute(stmt)
    sessions = res.scalars().all()
    return [
        {
            "id": s.id,
            "title": s.title,
            "status": s.status,
            "created_at": s.created_at.isoformat()
        }
        for s in sessions
    ]


@router.get("/sessions/{session_id}")
async def get_session_details(
    session_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(SearchSession)
        .where(SearchSession.id == session_id, SearchSession.user_id == current_user.id)
    )
    res = await db.execute(stmt)
    session_obj = res.scalar_one_or_none()
    if not session_obj:
        raise HTTPException(status_code=404, detail="Search session not found or unauthorized")

    return {
        "id": session_obj.id,
        "title": session_obj.title,
        "status": session_obj.status,
        "created_at": session_obj.created_at.isoformat(),
    }
