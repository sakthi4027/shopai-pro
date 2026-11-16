from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db
from backend.app.models.product import Product, ProductSpec
from backend.app.models.price import ProductPrice
from backend.app.schemas.product import ProductCompareRequest, ProductCompareResponse, ProductResponse, ProductSpecSchema

router = APIRouter(prefix="/compare", tags=["Product Comparison"])


@router.post("", response_model=ProductCompareResponse)
async def compare_products(req: ProductCompareRequest, db: AsyncSession = Depends(get_db)):
    if not req.product_ids:
        raise HTTPException(status_code=400, detail="At least one product_id must be provided for comparison.")

    stmt = select(Product).where(Product.id.in_(req.product_ids))
    res = await db.execute(stmt)
    products = res.scalars().all()

    if not products:
        raise HTTPException(status_code=404, detail="No matching products found for the provided IDs.")

    product_responses = []
    prod_dict_list = []

    for p in products:
        spec_stmt = select(ProductSpec).where(ProductSpec.product_id == p.id)
        spec_res = await db.execute(spec_stmt)
        spec = spec_res.scalar_one_or_none()

        price_stmt = select(ProductPrice).where(ProductPrice.product_id == p.id).order_by(ProductPrice.current_price.asc())
        price_res = await db.execute(price_stmt)
        best_price_row = price_res.scalars().first()

        best_price = best_price_row.current_price if best_price_row else 0.0

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
            best_price=best_price,
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
        product_responses.append(p_resp)
        prod_dict_list.append({
            "id": p.id,
            "name": p.name,
            "price": best_price,
            "rating": p.rating,
            "ram": spec.ram_gb if spec else 0,
            "storage": spec.storage_gb if spec else 0,
            "cpu": spec.cpu if spec else "N/A",
            "gpu": spec.gpu if spec else "N/A",
            "battery": spec.battery_life_hours if spec else 0,
            "warranty": f"{spec.warranty_months} Months" if spec and spec.warranty_months else "12 Months"
        })

    # Construct feature matrix
    matrix_rows = [
        {"feature": "Price", "values": {p["id"]: f"₹{p['price']:,.0f}" for p in prod_dict_list}},
        {"feature": "RAM", "values": {p["id"]: f"{p['ram']}GB DDR5" for p in prod_dict_list}},
        {"feature": "Storage", "values": {p["id"]: f"{p['storage']}GB SSD" for p in prod_dict_list}},
        {"feature": "Processor", "values": {p["id"]: p["cpu"] for p in prod_dict_list}},
        {"feature": "Graphics", "values": {p["id"]: p["gpu"] for p in prod_dict_list}},
        {"feature": "Battery Life", "values": {p["id"]: f"~{p['battery']} Hours" for p in prod_dict_list}},
        {"feature": "Rating", "values": {p["id"]: f"⭐ {p['rating']} / 5.0" for p in prod_dict_list}},
        {"feature": "Warranty", "values": {p["id"]: p["warranty"] for p in prod_dict_list}}
    ]

    # Evaluate Highlights
    best_rated = max(prod_dict_list, key=lambda x: x["rating"])["name"]
    cheapest = min(prod_dict_list, key=lambda x: x["price"])["name"]
    best_perf = max(prod_dict_list, key=lambda x: (x["ram"] + (40 if "4060" in x["gpu"] else 20)))["name"]
    best_value = max(prod_dict_list, key=lambda x: (x["ram"] / max(x["price"], 1.0)))["name"]

    highlights = {
        "best_overall": best_perf,
        "best_value": best_value,
        "best_performance": best_perf,
        "cheapest_suitable": cheapest,
        "best_rated": best_rated
    }

    return ProductCompareResponse(
        products=product_responses,
        comparison_matrix=matrix_rows,
        highlights=highlights
    )
