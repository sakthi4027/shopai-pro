import uuid
import json
import asyncio
from datetime import datetime
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload

from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.models.conversation import Conversation, Message, SearchSource
from backend.app.models.preference import UserPreference
from backend.app.models.agent_log import AuditLog
from backend.app.schemas.conversation import (
    CreateConversationRequest,
    SendMessageRequest,
    ConversationSummaryResponse,
    ConversationDetailResponse,
    MessageResponse,
    CheckoutIntentRequest,
    CheckoutManifestResponse
)
from backend.app.security.dependencies import get_current_user
from backend.app.services.stream_manager import stream_manager
from agents.orchestrator.agent import orchestrator_agent

router = APIRouter(prefix="/conversations", tags=["Conversational AI Shopping Agent"])


@router.get("", response_model=List[ConversationSummaryResponse])
async def list_conversations(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List all conversational research threads for the authenticated user."""
    stmt = (
        select(Conversation)
        .where(Conversation.user_id == current_user.id)
        .options(selectinload(Conversation.messages))
        .order_by(desc(Conversation.updated_at))
    )
    res = await db.execute(stmt)
    convs = res.scalars().all()
    
    return [
        ConversationSummaryResponse(
            id=c.id,
            title=c.title,
            search_mode=c.search_mode,
            created_at=c.created_at,
            updated_at=c.updated_at,
            message_count=len(c.messages)
        )
        for c in convs
    ]


@router.post("", response_model=ConversationDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_conversation(
    req: CreateConversationRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Start a fresh conversational AI shopping research session."""
    conv = Conversation(
        id=str(uuid.uuid4()),
        user_id=current_user.id,
        title=req.title or "New Shopping Research",
        search_mode=req.search_mode or "deep",
        active_constraints={},
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(conv)
    await db.commit()
    await db.refresh(conv)

    return ConversationDetailResponse(
        id=conv.id,
        title=conv.title,
        search_mode=conv.search_mode,
        active_constraints=conv.active_constraints or {},
        created_at=conv.created_at,
        updated_at=conv.updated_at,
        messages=[]
    )


@router.get("/{id}", response_model=ConversationDetailResponse)
async def get_conversation(
    id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Retrieve conversation details with full message history and multi-turn constraints."""
    stmt = (
        select(Conversation)
        .where(Conversation.id == id, Conversation.user_id == current_user.id)
        .options(selectinload(Conversation.messages))
    )
    res = await db.execute(stmt)
    conv = res.scalar_one_or_none()
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")

    messages_sorted = sorted(conv.messages, key=lambda m: m.created_at)
    return ConversationDetailResponse(
        id=conv.id,
        title=conv.title,
        search_mode=conv.search_mode,
        active_constraints=conv.active_constraints or {},
        created_at=conv.created_at,
        updated_at=conv.updated_at,
        messages=[
            MessageResponse(
                id=m.id,
                conversation_id=m.conversation_id,
                role=m.role,
                content=m.content,
                agent_steps=m.agent_steps or [],
                sources_status=m.sources_status or [],
                products_payload=m.products_payload or [],
                total_products_found=m.total_products_found or 0,
                comparison_payload=m.comparison_payload or {},
                follow_up_suggestions=m.follow_up_suggestions or [],
                created_at=m.created_at
            )
            for m in messages_sorted
        ]
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conversation(
    id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete a conversation thread and its associated message history."""
    stmt = select(Conversation).where(Conversation.id == id, Conversation.user_id == current_user.id)
    res = await db.execute(stmt)
    conv = res.scalar_one_or_none()
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")

    await db.delete(conv)
    await db.commit()
    return None


@router.post("/{id}/messages", response_model=MessageResponse)
async def send_message(
    id: str,
    req: SendMessageRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    User sends a natural-language shopping query or follow-up.
    Executes the deep multi-agent research workflow, preserves multi-turn memory,
    streams real-time thinking progress, and returns structured product recommendations.
    """
    stmt = (
        select(Conversation)
        .where(Conversation.id == id, Conversation.user_id == current_user.id)
        .options(selectinload(Conversation.messages))
    )
    res = await db.execute(stmt)
    conv = res.scalar_one_or_none()
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")

    # 1. Persist User Message
    user_msg = Message(
        id=str(uuid.uuid4()),
        conversation_id=conv.id,
        role="user",
        content=req.content,
        created_at=datetime.utcnow()
    )
    db.add(user_msg)
    await db.flush()

    # 2. Fetch User Shopping Memory
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

    # 3. Setup Telemetry & Event Streaming
    agent_steps = []

    async def on_event(agent: str, event_status: str, message: str, payload: Optional[Dict[str, Any]] = None):
        step_entry = {
            "agent": agent,
            "status": event_status,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }
        agent_steps.append(step_entry)
        await stream_manager.broadcast_event(conv.id, step_entry)

    # 4. Execute Multi-Agent Orchestrator
    search_mode = req.search_mode or conv.search_mode or "deep"
    result = await orchestrator_agent.execute_workflow(
        query=req.content,
        user_preferences=user_prefs_dict,
        active_constraints=conv.active_constraints or {},
        search_mode=search_mode,
        on_event=on_event
    )

    # 5. Update Conversation Memory & Title
    plan = result.get("plan", {})
    new_constraints = dict(conv.active_constraints or {})
    if plan.get("category"):
        new_constraints["category"] = plan["category"]
    if plan.get("budget_max"):
        new_constraints["budget_max"] = plan["budget_max"]
    if plan.get("required_features"):
        new_constraints["required_features"] = plan["required_features"]
    if plan.get("preferred_brands"):
        new_constraints["preferred_brands"] = plan["preferred_brands"]

    conv.active_constraints = new_constraints
    conv.updated_at = datetime.utcnow()

    if conv.title == "New Shopping Research" or not conv.title:
        words = req.content.strip().split()
        short_title = " ".join(words[:6])
        conv.title = short_title[:45] + ("..." if len(short_title) > 45 else "")

    # 6. Persist Assistant Message
    assistant_msg = Message(
        id=str(uuid.uuid4()),
        conversation_id=conv.id,
        role="assistant",
        content=result.get("conversational_content", "I searched available sources for your request."),
        agent_steps=agent_steps,
        sources_status=result.get("sources_status", []),
        products_payload=result.get("ranked_products", []),
        total_products_found=result.get("total_products_found", len(result.get("ranked_products", []))),
        comparison_payload={
            "matrix": result.get("comparison_matrix", []),
            "highlights": result.get("comparison_highlights", {})
        },
        follow_up_suggestions=result.get("follow_up_suggestions", []),
        created_at=datetime.utcnow()
    )
    db.add(assistant_msg)

    # Audit Log
    db.add(AuditLog(
        user_id=current_user.id,
        action="conversational_search_message",
        resource_type="conversation",
        resource_id=conv.id,
        details={
            "conversation_id": conv.id,
            "query": req.content,
            "mode": search_mode,
            "products_returned": len(result.get("ranked_products", []))
        }
    ))

    await db.commit()
    await db.refresh(assistant_msg)

    return MessageResponse(
        id=assistant_msg.id,
        conversation_id=assistant_msg.conversation_id,
        role=assistant_msg.role,
        content=assistant_msg.content,
        agent_steps=assistant_msg.agent_steps or [],
        sources_status=assistant_msg.sources_status or [],
        products_payload=assistant_msg.products_payload or [],
        total_products_found=assistant_msg.total_products_found or 0,
        comparison_payload=assistant_msg.comparison_payload or {},
        follow_up_suggestions=assistant_msg.follow_up_suggestions or [],
        created_at=assistant_msg.created_at
    )


@router.get("/{id}/stream")
async def stream_conversation_events(
    id: str,
    token: Optional[str] = Query(None)
):
    """
    Server-Sent Events (SSE) endpoint to receive live real-time agent execution events,
    tool calls, and search discovery updates in real time.
    """
    queue = stream_manager.register_sse_queue(id)

    async def event_generator():
        try:
            # Yield initial connect event
            yield f"data: {json.dumps({'type': 'connected', 'conversation_id': id})}\n\n"
            while True:
                try:
                    event = await asyncio.wait_for(queue.get(), timeout=25.0)
                    yield f"data: {json.dumps(event)}\n\n"
                except asyncio.TimeoutError:
                    # Keep-alive heartbeat comment
                    yield ": ping\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            stream_manager.unregister_sse_queue(id, queue)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


@router.post("/checkout-intent", response_model=CheckoutManifestResponse)
async def request_checkout_intent(
    req: CheckoutIntentRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Strict Human-In-The-Loop Checkout Gate:
    Generates an itemized pre-purchase manifest that requires explicit human confirmation.
    Zero autonomous purchasing: We never store payment card credentials or complete financial transactions.
    """
    total = req.price + req.shipping_cost
    
    # Audit trail
    db.add(AuditLog(
        user_id=current_user.id,
        action="human_checkout_gate_intent",
        resource_type="checkout",
        details={
            "product_name": req.product_name,
            "seller": req.seller_name,
            "total_cost": total,
            "status": "awaiting_human_confirmation"
        }
    ))
    await db.commit()

    return CheckoutManifestResponse(
        confirmation_required=True,
        notice="⚠️ HUMAN CONFIRMATION REQUIRED BEFORE PURCHASE ASSISTANCE",
        product_name=req.product_name,
        price=req.price,
        seller_name=req.seller_name,
        shipping_cost=req.shipping_cost,
        total_cost=total,
        currency="INR",
        checkout_url=req.product_url,
        security_guarantee="Strict zero-autonomous-purchase guarantee. We never store credit card or payment information."
    )
