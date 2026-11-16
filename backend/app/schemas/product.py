from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime


class ProductSpecSchema(BaseModel):
    ram_gb: Optional[int] = None
    storage_gb: Optional[int] = None
    cpu: Optional[str] = None
    gpu: Optional[str] = None
    screen_size_inches: Optional[float] = None
    battery_life_hours: Optional[float] = None
    os: Optional[str] = None
    weight_kg: Optional[float] = None
    warranty_months: Optional[int] = None
    raw_specs: Dict[str, Any] = {}

    class Config:
        from_attributes = True


class SellerPriceSchema(BaseModel):
    id: str
    seller_name: str
    platform: str
    seller_rating: float
    current_price: float
    original_price: Optional[float] = None
    discount_percentage: float = 0.0
    currency: str = "INR"
    availability: str = "In Stock"
    shipping_cost: float = 0.0
    estimated_delivery: str = "2-4 days"


class ProductResponse(BaseModel):
    id: str
    name: str
    brand: Optional[str] = None
    model: Optional[str] = None
    category: str
    description: Optional[str] = None
    main_image: Optional[str] = None
    product_url: Optional[str] = None
    source: str
    rating: float = 0.0
    review_count: int = 0
    trust_score: float = 1.0
    trust_warning: Optional[str] = None
    is_verified: bool = True
    best_price: Optional[float] = None
    currency: str = "INR"
    availability: str = "In Stock"
    specs: Optional[ProductSpecSchema] = None
    last_checked: datetime

    class Config:
        from_attributes = True


class ProductDetailResponse(ProductResponse):
    prices: List[SellerPriceSchema] = []
    price_history: List[Dict[str, Any]] = []


class ProductCompareRequest(BaseModel):
    product_ids: List[str]


class ProductCompareResponse(BaseModel):
    products: List[ProductResponse]
    comparison_matrix: List[Dict[str, Any]]
    highlights: Dict[str, Optional[str]] = {
        "best_overall": None,
        "best_value": None,
        "best_performance": None,
        "cheapest_suitable": None,
        "best_rated": None
    }
