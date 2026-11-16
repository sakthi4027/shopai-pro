import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from backend.app.database.session import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    request_id = Column(String(36), ForeignKey("shopping_requests.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id = Column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Mathematical Multi-Factor Scores (0 - 100)
    score_overall = Column(Float, nullable=False, index=True)
    score_match = Column(Float, nullable=False)
    score_price = Column(Float, nullable=False)
    score_performance = Column(Float, nullable=False)
    score_reviews = Column(Float, nullable=False)
    
    # Classification Badge: "Best Overall", "Best Value", "Best Performance", "Cheapest Suitable", "None"
    badge = Column(String(50), nullable=True, index=True)
    budget_status = Column(String(50), default="Within Budget")  # "Within Budget", "Near Budget", "Over Budget"
    
    explanation = Column(Text, nullable=False)
    breakdown = Column(JSON, default=dict)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    request = relationship("ShoppingRequest", back_populates="recommendations")
    product = relationship("Product", back_populates="recommendations")
