import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from backend.app.database.session import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    product_id = Column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    
    source = Column(String(100), nullable=False)  # "Amazon India", "Flipkart", "Reddit", "YouTube"
    author = Column(String(100), nullable=True)
    rating = Column(Float, nullable=False)
    title = Column(String(255), nullable=True)
    review_text = Column(Text, nullable=False)
    sentiment = Column(String(20), nullable=True)  # "Positive", "Neutral", "Negative"
    review_date = Column(DateTime, default=datetime.utcnow)

    # Relationships
    product = relationship("Product", back_populates="reviews")


class ReviewAnalysis(Base):
    __tablename__ = "review_analysis"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    product_id = Column(String(36), ForeignKey("products.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    
    sentiment_positive_pct = Column(Float, default=0.0)
    sentiment_neutral_pct = Column(Float, default=0.0)
    sentiment_negative_pct = Column(Float, default=0.0)
    
    # Themes analyzed across key aspects: battery, performance, display, thermals, build quality, software
    positive_themes = Column(JSON, default=list)
    negative_themes = Column(JSON, default=list)
    common_complaints = Column(JSON, default=list)
    important_warnings = Column(JSON, default=list)
    
    aspect_scores = Column(JSON, default=dict)  # {"battery": 4.2, "performance": 4.8, "heating": 3.6, ...}
    analyzed_review_count = Column(Float, default=0)
    last_analyzed = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    product = relationship("Product", back_populates="review_analyses")
