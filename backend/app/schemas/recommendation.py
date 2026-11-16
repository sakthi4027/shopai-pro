from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime
from backend.app.schemas.product import ProductResponse


class RecommendationItem(BaseModel):
    id: str
    product: ProductResponse
    score_overall: float
    score_match: float
    score_price: float
    score_performance: float
    score_reviews: float
    badge: Optional[str] = None
    budget_status: str = "Within Budget"
    explanation: str
    breakdown: Dict[str, Any] = {}

    class Config:
        from_attributes = True


class RecommendationResponse(BaseModel):
    request_id: str
    top_recommendations: List[RecommendationItem] = []
    best_overall: Optional[RecommendationItem] = None
    best_value: Optional[RecommendationItem] = None
    best_performance: Optional[RecommendationItem] = None
    cheapest_suitable: Optional[RecommendationItem] = None
