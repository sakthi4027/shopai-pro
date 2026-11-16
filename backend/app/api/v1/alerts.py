import uuid
from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.models.product import Product
from backend.app.models.price import ProductPrice
from backend.app.models.user_data import Alert
from backend.app.security.dependencies import get_current_user

router = APIRouter(prefix="/alerts", tags=["Price Alerts"])


class CreateAlertRequest(BaseModel):
    product_id: str
    target_price: float
    alert_type: str = "price_drop"


@router.get("")
async def get_alerts(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Alert, Product)
        .join(Product, Alert.product_id == Product.id)
        .where(Alert.user_id == current_user.id)
        .order_by(Alert.created_at.desc())
    )
    res = await db.execute(stmt)
    rows = res.all()

    out = []
    for alert, p in rows:
        # Get current price
        price_stmt = select(ProductPrice).where(ProductPrice.product_id == p.id).order_by(ProductPrice.current_price.asc())
        price_res = await db.execute(price_stmt)
        pp = price_res.scalars().first()
        curr_price = pp.current_price if pp else 0.0

        out.append({
            "id": alert.id,
            "product_id": p.id,
            "product_name": p.name,
            "target_price": alert.target_price,
            "current_price": curr_price,
            "difference": round(curr_price - alert.target_price, 2),
            "currency": alert.currency,
            "is_triggered": alert.is_triggered or (curr_price <= alert.target_price and curr_price > 0),
            "created_at": alert.created_at.isoformat()
        })
    return out


@router.post("")
async def create_alert(
    req: CreateAlertRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    prod_stmt = select(Product).where(Product.id == req.product_id)
    prod_res = await db.execute(prod_stmt)
    p = prod_res.scalar_one_or_none()
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")

    new_alert = Alert(
        id=str(uuid.uuid4()),
        user_id=current_user.id,
        product_id=req.product_id,
        target_price=req.target_price,
        alert_type=req.alert_type,
        is_triggered=False
    )
    db.add(new_alert)
    await db.commit()
    return {
        "message": f"Price alert configured! We will notify you when price drops to or below ₹{req.target_price:,.0f}.",
        "id": new_alert.id
    }


@router.delete("/{alert_id}")
async def delete_alert(
    alert_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Alert).where(and_(Alert.id == alert_id, Alert.user_id == current_user.id))
    res = await db.execute(stmt)
    alert = res.scalar_one_or_none()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found or unauthorized")

    await db.delete(alert)
    await db.commit()
    return {"message": "Price alert deleted successfully"}
