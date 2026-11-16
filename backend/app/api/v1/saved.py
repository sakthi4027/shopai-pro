import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.models.product import Product
from backend.app.models.user_data import SavedProduct
from backend.app.security.dependencies import get_current_user

router = APIRouter(prefix="/saved", tags=["Saved Products"])


@router.get("")
async def get_saved_products(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(SavedProduct, Product)
        .join(Product, SavedProduct.product_id == Product.id)
        .where(SavedProduct.user_id == current_user.id)
        .order_by(SavedProduct.created_at.desc())
    )
    res = await db.execute(stmt)
    rows = res.all()

    return [
        {
            "id": sp.id,
            "product_id": p.id,
            "product_name": p.name,
            "brand": p.brand,
            "rating": p.rating,
            "main_image": p.main_image,
            "notes": sp.notes,
            "saved_at": sp.created_at.isoformat()
        }
        for sp, p in rows
    ]


@router.post("/{product_id}")
async def save_product(
    product_id: str,
    notes: str = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Verify product exists
    prod_stmt = select(Product).where(Product.id == product_id)
    prod_res = await db.execute(prod_stmt)
    if not prod_res.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Product not found")

    # Check if already saved
    existing_stmt = select(SavedProduct).where(
        and_(SavedProduct.user_id == current_user.id, SavedProduct.product_id == product_id)
    )
    existing_res = await db.execute(existing_stmt)
    if existing_res.scalar_one_or_none():
        return {"message": "Product is already in your saved list."}

    sp = SavedProduct(
        id=str(uuid.uuid4()),
        user_id=current_user.id,
        product_id=product_id,
        notes=notes
    )
    db.add(sp)
    await db.commit()
    return {"message": "Product saved successfully", "id": sp.id}


@router.delete("/{product_id}")
async def remove_saved_product(
    product_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(SavedProduct).where(
        and_(SavedProduct.user_id == current_user.id, SavedProduct.product_id == product_id)
    )
    res = await db.execute(stmt)
    sp = res.scalar_one_or_none()
    if not sp:
        raise HTTPException(status_code=404, detail="Item not found in your saved list.")

    await db.delete(sp)
    await db.commit()
    return {"message": "Removed from saved products."}
