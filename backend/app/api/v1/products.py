from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from backend.app.database.session import get_db
from backend.app.models.product import Product, ProductSpec, ProductVariant
from backend.app.models.price import ProductPrice, Seller, PriceHistory
from backend.app.schemas.product import ProductResponse, ProductDetailResponse, ProductSpecSchema, SellerPriceSchema

router = APIRouter(prefix="/products", tags=["Product Catalog"])


@router.get("", response_model=List[ProductResponse])
async def list_products(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    search: Optional[str] = None,
    limit: int = Query(default=20, le=50),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Product)
    filters = []

    if category:
        filters.append(Product.category == category)
    if brand:
        filters.append(Product.brand.ilike(f"%{brand}%"))
    if search:
        filters.append(Product.name.ilike(f"%{search}%"))

    if filters:
        stmt = stmt.where(and_(*filters))

    stmt = stmt.limit(limit)
    res = await db.execute(stmt)
    products = res.scalars().all()

    out = []
    for p in products:
        # Load spec
        spec_stmt = select(ProductSpec).where(ProductSpec.product_id == p.id)
        spec_res = await db.execute(spec_stmt)
        spec = spec_res.scalar_one_or_none()

        # Load best price
        price_stmt = select(ProductPrice).where(ProductPrice.product_id == p.id).order_by(ProductPrice.current_price.asc())
        price_res = await db.execute(price_stmt)
        best_price_row = price_res.scalars().first()

        out.append(ProductResponse(
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
            currency=best_price_row.currency if best_price_row else "INR",
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
        ))
    return out


@router.get("/{product_id}", response_model=ProductDetailResponse)
async def get_product_detail(product_id: str, db: AsyncSession = Depends(get_db)):
    stmt = select(Product).where(Product.id == product_id)
    res = await db.execute(stmt)
    p = res.scalar_one_or_none()
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")

    # Load Spec
    spec_stmt = select(ProductSpec).where(ProductSpec.product_id == p.id)
    spec_res = await db.execute(spec_stmt)
    spec = spec_res.scalar_one_or_none()

    # Load Prices & Sellers
    price_stmt = select(ProductPrice, Seller).join(Seller, ProductPrice.seller_id == Seller.id).where(ProductPrice.product_id == p.id)
    price_res = await db.execute(price_stmt)
    price_rows = price_res.all()

    sellers_list = []
    best_price = None
    for pp, sel in price_rows:
        if best_price is None or pp.current_price < best_price:
            best_price = pp.current_price
        sellers_list.append(SellerPriceSchema(
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

    # Load Price History
    hist_stmt = select(PriceHistory).where(PriceHistory.product_id == p.id).order_by(PriceHistory.recorded_at.asc())
    hist_res = await db.execute(hist_stmt)
    hist_rows = hist_res.scalars().all()
    history_data = [{"date": h.recorded_at.strftime("%Y-%m-%d"), "price": h.price} for h in hist_rows]

    return ProductDetailResponse(
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
        best_price=best_price,
        currency="INR",
        availability="In Stock",
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
        last_checked=p.last_checked,
        prices=sellers_list,
        price_history=history_data
    )
