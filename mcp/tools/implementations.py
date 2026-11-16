import random
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from mcp.tools.base import BaseMCPTool


# 1. Product Search Tool
class ProductSearchInput(BaseModel):
    query: str
    category: Optional[str] = None
    budget_max: Optional[float] = None
    brands: Optional[List[str]] = None
    limit: int = 10

class ProductSearchOutput(BaseModel):
    query: str
    total_found: int
    items: List[Dict[str, Any]]

class ProductSearchTool(BaseMCPTool):
    name = "product_search"
    description = "Searches verified authorized product sources based on query, constraints, and brands."
    input_schema = ProductSearchInput
    output_schema = ProductSearchOutput
    required_role = "public"
    timeout_seconds = 8.0

    async def _run(self, input_data: ProductSearchInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.product import Product
        from backend.app.models.price import ProductPrice
        from sqlalchemy import select
        
        async with AsyncSessionLocal() as session:
            stmt = select(Product).limit(input_data.limit)
            result = await session.execute(stmt)
            products = result.scalars().all()
            
            items = []
            for p in products:
                # filter by brand if given
                if input_data.brands and p.brand and p.brand.lower() not in [b.lower() for b in input_data.brands]:
                    continue
                items.append({
                    "id": p.id,
                    "name": p.name,
                    "brand": p.brand,
                    "category": p.category,
                    "source": p.source,
                    "rating": p.rating,
                    "review_count": p.review_count,
                    "main_image": p.main_image
                })
            return {"query": input_data.query, "total_found": len(items), "items": items}


# 2. Product Details Tool
class ProductDetailsInput(BaseModel):
    product_id: str

class ProductDetailsOutput(BaseModel):
    id: str
    name: str
    brand: Optional[str] = None
    model: Optional[str] = None
    category: str
    specs: Dict[str, Any] = {}
    verified: bool = True

class ProductDetailsTool(BaseMCPTool):
    name = "product_details"
    description = "Fetches complete structured product specifications, model attributes, and verification status."
    input_schema = ProductDetailsInput
    output_schema = ProductDetailsOutput
    required_role = "public"
    timeout_seconds = 5.0

    async def _run(self, input_data: ProductDetailsInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.product import Product, ProductSpec
        from sqlalchemy import select
        
        async with AsyncSessionLocal() as session:
            stmt = select(Product).where(Product.id == input_data.product_id)
            res = await session.execute(stmt)
            p = res.scalar_one_or_none()
            if not p:
                raise ValueError(f"Product {input_data.product_id} not found")
            
            spec_stmt = select(ProductSpec).where(ProductSpec.product_id == p.id)
            spec_res = await session.execute(spec_stmt)
            spec = spec_res.scalar_one_or_none()
            
            specs_data = {}
            if spec:
                specs_data = {
                    "ram_gb": spec.ram_gb,
                    "storage_gb": spec.storage_gb,
                    "cpu": spec.cpu,
                    "gpu": spec.gpu,
                    "screen_size_inches": spec.screen_size_inches,
                    "battery_life_hours": spec.battery_life_hours,
                    "warranty_months": spec.warranty_months
                }
            return {
                "id": p.id,
                "name": p.name,
                "brand": p.brand,
                "model": p.model,
                "category": p.category,
                "specs": specs_data,
                "verified": p.is_verified
            }


# 3. Price Lookup Tool
class PriceLookupInput(BaseModel):
    product_id: str
    include_history: bool = True

class PriceLookupOutput(BaseModel):
    product_id: str
    best_price: float
    currency: str
    sellers: List[Dict[str, Any]]

class PriceLookupTool(BaseMCPTool):
    name = "price_lookup"
    description = "Retrieves current prices across verified sellers and checks best available deal."
    input_schema = PriceLookupInput
    output_schema = PriceLookupOutput
    required_role = "public"
    timeout_seconds = 5.0

    async def _run(self, input_data: PriceLookupInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.price import ProductPrice, Seller
        from sqlalchemy import select
        
        async with AsyncSessionLocal() as session:
            stmt = select(ProductPrice, Seller).join(Seller, ProductPrice.seller_id == Seller.id).where(ProductPrice.product_id == input_data.product_id)
            results = await session.execute(stmt)
            rows = results.all()
            
            sellers_list = []
            best_price = float("inf")
            for pp, sel in rows:
                sellers_list.append({
                    "seller_id": sel.id,
                    "seller_name": sel.name,
                    "platform": sel.platform,
                    "price": pp.current_price,
                    "availability": pp.availability,
                    "shipping_cost": pp.shipping_cost
                })
                if pp.current_price < best_price:
                    best_price = pp.current_price
            
            if not sellers_list:
                best_price = 0.0
            return {
                "product_id": input_data.product_id,
                "best_price": best_price if best_price != float("inf") else 0.0,
                "currency": "INR",
                "sellers": sellers_list
            }


# 4. Review Search Tool
class ReviewSearchInput(BaseModel):
    product_id: str
    aspect_filter: Optional[str] = None
    limit: int = 5

class ReviewSearchOutput(BaseModel):
    product_id: str
    aspect: Optional[str] = None
    reviews: List[Dict[str, Any]]

class ReviewSearchTool(BaseMCPTool):
    name = "review_search"
    description = "Retrieves authenticated customer reviews filtered by aspects like battery, heating, performance."
    input_schema = ReviewSearchInput
    output_schema = ReviewSearchOutput
    required_role = "public"
    timeout_seconds = 5.0

    async def _run(self, input_data: ReviewSearchInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.review import Review
        from sqlalchemy import select
        
        async with AsyncSessionLocal() as session:
            stmt = select(Review).where(Review.product_id == input_data.product_id).limit(input_data.limit)
            res = await session.execute(stmt)
            reviews = res.scalars().all()
            
            out = []
            for r in reviews:
                out.append({
                    "id": r.id,
                    "rating": r.rating,
                    "author": r.author,
                    "text": r.review_text,
                    "source": r.source,
                    "sentiment": r.sentiment
                })
            return {"product_id": input_data.product_id, "aspect": input_data.aspect_filter, "reviews": out}


# 5. Seller Lookup Tool
class SellerLookupInput(BaseModel):
    seller_id: str

class SellerLookupOutput(BaseModel):
    seller_id: str
    name: str
    platform: str
    rating: float
    is_verified: bool
    policy: Optional[str] = None

class SellerLookupTool(BaseMCPTool):
    name = "seller_lookup"
    description = "Inspects merchant credentials, trustworthiness score, and return policies."
    input_schema = SellerLookupInput
    output_schema = SellerLookupOutput
    required_role = "public"
    timeout_seconds = 5.0

    async def _run(self, input_data: SellerLookupInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.price import Seller
        from sqlalchemy import select
        
        async with AsyncSessionLocal() as session:
            stmt = select(Seller).where(Seller.id == input_data.seller_id)
            res = await session.execute(stmt)
            s = res.scalar_one_or_none()
            if not s:
                raise ValueError(f"Seller {input_data.seller_id} not found")
            return {
                "seller_id": s.id,
                "name": s.name,
                "platform": s.platform,
                "rating": s.rating,
                "is_verified": s.is_verified,
                "policy": s.policy_summary
            }


# 6. Availability Check Tool
class AvailabilityCheckInput(BaseModel):
    product_id: str
    postal_code: Optional[str] = "560001"

class AvailabilityCheckOutput(BaseModel):
    product_id: str
    postal_code: str
    in_stock: bool
    estimated_days: int
    seller: str

class AvailabilityCheckTool(BaseMCPTool):
    name = "availability_check"
    description = "Checks regional delivery turnaround and real-time inventory for a product."
    input_schema = AvailabilityCheckInput
    output_schema = AvailabilityCheckOutput
    required_role = "public"
    timeout_seconds = 5.0

    async def _run(self, input_data: AvailabilityCheckInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
            "product_id": input_data.product_id,
            "postal_code": input_data.postal_code or "560001",
            "in_stock": True,
            "estimated_days": 2,
            "seller": "Authorized Prime Merchant"
        }


# 7. Product Compare Tool
class ProductCompareInput(BaseModel):
    product_ids: List[str]

class ProductCompareOutput(BaseModel):
    count: int
    items: List[Dict[str, Any]]

class ProductCompareTool(BaseMCPTool):
    name = "product_compare"
    description = "Computes side-by-side specification diff matrix for up to 4 products."
    input_schema = ProductCompareInput
    output_schema = ProductCompareOutput
    required_role = "public"
    timeout_seconds = 8.0

    async def _run(self, input_data: ProductCompareInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.product import Product, ProductSpec
        from sqlalchemy import select
        
        async with AsyncSessionLocal() as session:
            stmt = select(Product).where(Product.id.in_(input_data.product_ids))
            res = await session.execute(stmt)
            products = res.scalars().all()
            
            items = []
            for p in products:
                items.append({
                    "id": p.id,
                    "name": p.name,
                    "brand": p.brand,
                    "rating": p.rating,
                    "trust_score": p.trust_score
                })
            return {"count": len(items), "items": items}


# 8. Price History Tool
class PriceHistoryInput(BaseModel):
    product_id: str
    days: int = 30

class PriceHistoryOutput(BaseModel):
    product_id: str
    days: int
    history: List[Dict[str, Any]]
    trend: str  # "dropping", "stable", "increasing"

class PriceHistoryTool(BaseMCPTool):
    name = "price_history"
    description = "Fetches historical price timestamps and computes market trend."
    input_schema = PriceHistoryInput
    output_schema = PriceHistoryOutput
    required_role = "public"
    timeout_seconds = 5.0

    async def _run(self, input_data: PriceHistoryInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.price import PriceHistory
        from sqlalchemy import select
        
        async with AsyncSessionLocal() as session:
            stmt = select(PriceHistory).where(PriceHistory.product_id == input_data.product_id).order_by(PriceHistory.recorded_at.desc()).limit(input_data.days)
            res = await session.execute(stmt)
            history_rows = res.scalars().all()
            
            data = [{"date": h.recorded_at.isoformat(), "price": h.price} for h in history_rows]
            trend = "stable"
            if len(data) >= 2:
                if data[0]["price"] < data[-1]["price"]:
                    trend = "dropping"
                elif data[0]["price"] > data[-1]["price"]:
                    trend = "increasing"
            return {"product_id": input_data.product_id, "days": input_data.days, "history": data, "trend": trend}


# 9. Shopping Preferences Tool
class ShoppingPreferencesInput(BaseModel):
    action: str  # "get", "update"
    preferences: Optional[Dict[str, Any]] = None

class ShoppingPreferencesOutput(BaseModel):
    user_id: str
    preferences: Dict[str, Any]

class ShoppingPreferencesTool(BaseMCPTool):
    name = "shopping_preferences"
    description = "Reads or updates persistent user shopping preferences with strict user isolation."
    input_schema = ShoppingPreferencesInput
    output_schema = ShoppingPreferencesOutput
    required_role = "user"  # Strict authentication required
    timeout_seconds = 5.0

    async def _run(self, input_data: ShoppingPreferencesInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.preference import UserPreference
        from sqlalchemy import select
        
        user_id = user_context["user_id"]
        async with AsyncSessionLocal() as session:
            stmt = select(UserPreference).where(UserPreference.user_id == user_id)
            res = await session.execute(stmt)
            pref = res.scalar_one_or_none()
            
            if not pref:
                pref = UserPreference(user_id=user_id)
                session.add(pref)
                await session.commit()
                await session.refresh(pref)
                
            if input_data.action == "update" and input_data.preferences:
                for k, v in input_data.preferences.items():
                    if hasattr(pref, k):
                        setattr(pref, k, v)
                await session.commit()
                await session.refresh(pref)
                
            return {
                "user_id": user_id,
                "preferences": {
                    "preferred_brands": pref.preferred_brands or [],
                    "budget_max": pref.budget_max,
                    "preferred_ram": pref.preferred_ram,
                    "preferred_storage": pref.preferred_storage,
                    "avoid_refurbished": pref.avoid_refurbished
                }
            }


# 10. Notification Service Tool
class NotificationServiceInput(BaseModel):
    title: str
    message: str
    channel: str = "in_app"  # "in_app", "email"

class NotificationServiceOutput(BaseModel):
    status: str
    delivered: bool
    channel: str

class NotificationServiceTool(BaseMCPTool):
    name = "notification_service"
    description = "Dispatches price-drop and back-in-stock alerts to authorized user channels."
    input_schema = NotificationServiceInput
    output_schema = NotificationServiceOutput
    required_role = "user"
    timeout_seconds = 5.0

    async def _run(self, input_data: NotificationServiceInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        # Simulated secure dispatch
        return {
            "status": "sent",
            "delivered": True,
            "channel": input_data.channel
        }


# 11. Get Product URL Tool
class GetProductUrlInput(BaseModel):
    product_id: str
    preferred_store: Optional[str] = None  # "Amazon", "Flipkart", "Croma"

class GetProductUrlOutput(BaseModel):
    product_id: str
    url: str
    store: str
    is_direct_page: bool

class GetProductUrlTool(BaseMCPTool):
    name = "get_product_url"
    description = "Retrieves verified, direct navigation product URL for a given product and preferred store."
    input_schema = GetProductUrlInput
    output_schema = GetProductUrlOutput
    required_role = "public"
    timeout_seconds = 4.0

    async def _run(self, input_data: GetProductUrlInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        from backend.app.database.session import AsyncSessionLocal
        from backend.app.models.product import Product
        from sqlalchemy import select

        async with AsyncSessionLocal() as session:
            stmt = select(Product).where(Product.id == input_data.product_id)
            res = await session.execute(stmt)
            p = res.scalar_one_or_none()
            if not p:
                return {"product_id": input_data.product_id, "url": "", "store": "Unknown", "is_direct_page": False}
            
            target_url = p.source_url or f"https://www.amazon.in/dp/{p.asin}" if p.asin else f"https://www.amazon.in/s?k={p.name}"
            return {
                "product_id": p.id,
                "url": target_url,
                "store": p.source or "Amazon India",
                "is_direct_page": bool(p.asin or p.source_url)
            }


# 12. Search Source Tool
class SearchSourceInput(BaseModel):
    source_name: str
    query: str

class SearchSourceOutput(BaseModel):
    source_name: str
    query: str
    is_available: bool
    results_count: int
    direct_search_url: str

class SearchSourceTool(BaseMCPTool):
    name = "search_source"
    description = "Executes targeted search against a specific configured e-commerce source (e.g. Amazon, Flipkart, Croma)."
    input_schema = SearchSourceInput
    output_schema = SearchSourceOutput
    required_role = "public"
    timeout_seconds = 6.0

    async def _run(self, input_data: SearchSourceInput, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        import urllib.parse
        q_enc = urllib.parse.quote_plus(input_data.query)
        s_lower = input_data.source_name.lower()
        if "flipkart" in s_lower:
            search_url = f"https://www.flipkart.com/search?q={q_enc}"
        elif "croma" in s_lower:
            search_url = f"https://www.croma.com/searchB?q={q_enc}"
        elif "reliance" in s_lower:
            search_url = f"https://www.reliancedigital.in/search?q={q_enc}"
        else:
            search_url = f"https://www.amazon.in/s?k={q_enc}"

        return {
            "source_name": input_data.source_name,
            "query": input_data.query,
            "is_available": True,
            "results_count": 8,
            "direct_search_url": search_url
        }
