from typing import Optional, List, Dict
from pydantic import BaseModel
from datetime import datetime


class ReviewSchema(BaseModel):
    id: str
    product_id: str
    source: str
    author: Optional[str] = None
    rating: float
    title: Optional[str] = None
    review_text: str
    sentiment: Optional[str] = None
    review_date: Optional[datetime] = None

    class Config:
        from_attributes = True


class ReviewAnalysisResponse(BaseModel):
    product_id: str
    sentiment_positive_pct: float
    sentiment_neutral_pct: float
    sentiment_negative_pct: float
    positive_themes: List[str] = []
    negative_themes: List[str] = []
    common_complaints: List[str] = []
    important_warnings: List[str] = []
    aspect_scores: Dict[str, float] = {}
    analyzed_review_count: int = 0
    last_analyzed: datetime

    class Config:
        from_attributes = True
