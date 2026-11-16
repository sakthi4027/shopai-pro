from typing import List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db
from backend.app.models.price import ProductPrice, Seller, PriceHistory
from backend.app.schemas.product import SellerPriceSchema

router = APIRouter(prefix="/prices", tags=["Price Intelligence"])


@router.get("/{product_id}/sellers", response_model=List[SellerPriceSchema])
async def get_seller_prices(product_id: str, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(ProductPrice, Seller)
        .join(Seller, ProductPrice.seller_id == Seller.id)
        .where(ProductPrice.product_id == product_id)
        .order_by(ProductPrice.current_price.asc())
    )
    res = await db.execute(stmt)
    rows = res.all()

    out = []
    for pp, sel in rows:
        out.append(SellerPriceSchema(
            id=pp.id,
            seller_name=sel.name,
            platform=sel.platform,
            seller_rating=sel.rating,
            current_price=pp.current_price,
            original_price=pp.original_price,
            discount_percentage=pp.discount_percentage,
            currency=pp.currency,
            availability=pp.availability,
            shipping_cost=pp.shipping_cost,
            estimated_delivery=pp.estimated_delivery_days
        ))
    return out


@router.get("/{product_id}/history")
async def get_price_history(product_id: str, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(PriceHistory)
        .where(PriceHistory.product_id == product_id)
        .order_by(PriceHistory.recorded_at.asc())
    )
    res = await db.execute(stmt)
    history_records = res.scalars().all()

    points = [
        {
            "date": h.recorded_at.strftime("%Y-%m-%d"),
            "price": h.price,
            "currency": h.currency
        }
        for h in history_records
    ]

    # Calculate verified price insight
    insight = "Prices have remained stable over the observed monitoring interval."
    if len(points) >= 2:
        diff = points[-1]["price"] - points[0]["price"]
        if diff < 0:
            insight = f"Current price appears lower than the previously observed price by ₹{abs(diff):,.0f}."
        elif diff > 0:
            insight = f"Current price appears higher than previous baseline by ₹{diff:,.0f}."

    return {
        "product_id": product_id,
        "history": points,
        "price_insight": insight
    }
