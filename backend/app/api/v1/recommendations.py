from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db
from backend.app.models.recommendation import Recommendation
from backend.app.models.product import Product, ProductSpec
from backend.app.models.price import ProductPrice
from backend.app.schemas.recommendation import RecommendationResponse, RecommendationItem
from backend.app.schemas.product import ProductResponse, ProductSpecSchema

router = APIRouter(prefix="/recommendations", tags=["AI Recommendations"])


@router.get("/{request_id}", response_model=RecommendationResponse)
async def get_recommendations_for_request(request_id: str, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(Recommendation, Product)
        .join(Product, Recommendation.product_id == Product.id)
        .where(Recommendation.request_id == request_id)
        .order_by(Recommendation.score_overall.desc())
    )
    res = await db.execute(stmt)
    rows = res.all()

    if not rows:
        raise HTTPException(status_code=404, detail="No recommendations found for this request ID.")

    items = []
    best_overall = None
    best_value = None
    best_perf = None
    cheapest = None

    for rec, p in rows:
        spec_stmt = select(ProductSpec).where(ProductSpec.product_id == p.id)
        spec_res = await db.execute(spec_stmt)
        spec = spec_res.scalar_one_or_none()

        price_stmt = select(ProductPrice).where(ProductPrice.product_id == p.id).order_by(ProductPrice.current_price.asc())
        price_res = await db.execute(price_stmt)
        best_price_row = price_res.scalars().first()

        p_resp = ProductResponse(
            id=p.id,
            name=p.name,
            brand=p.brand,
            model=p.model,
            category=p.category,
            description=p.description,
            main_image=p.main_image,
            product_url=p.product_url,
            source=p.source,
            rating=p.rating,
            review_count=p.review_count,
            trust_score=p.trust_score,
            trust_warning=p.trust_warning,
            is_verified=p.is_verified,
            best_price=best_price_row.current_price if best_price_row else None,
            currency="INR",
            availability=best_price_row.availability if best_price_row else "In Stock",
            specs=ProductSpecSchema(
                ram_gb=spec.ram_gb,
                storage_gb=spec.storage_gb,
                cpu=spec.cpu,
                gpu=spec.gpu,
                screen_size_inches=spec.screen_size_inches,
                battery_life_hours=spec.battery_life_hours,
                os=spec.os,
                weight_kg=spec.weight_kg,
                warranty_months=spec.warranty_months,
                raw_specs=spec.raw_specs or {}
            ) if spec else None,
            last_checked=p.last_checked
        )

        item = RecommendationItem(
            id=rec.id,
            product=p_resp,
            score_overall=rec.score_overall,
            score_match=rec.score_match,
            score_price=rec.score_price,
            score_performance=rec.score_performance,
            score_reviews=rec.score_reviews,
            badge=rec.badge,
            budget_status=rec.budget_status,
            explanation=rec.explanation,
            breakdown=rec.breakdown or {}
        )
        items.append(item)

        if rec.badge == "Best Overall" and not best_overall:
            best_overall = item
        elif rec.badge == "Best Value" and not best_value:
            best_value = item
        elif rec.badge == "Best Performance" and not best_perf:
            best_perf = item
        elif rec.badge == "Cheapest Suitable" and not cheapest:
            cheapest = item

    return RecommendationResponse(
        request_id=request_id,
        top_recommendations=items,
        best_overall=best_overall or (items[0] if items else None),
        best_value=best_value,
        best_performance=best_perf,
        cheapest_suitable=cheapest
    )
