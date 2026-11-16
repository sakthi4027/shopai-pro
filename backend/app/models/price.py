import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from backend.app.database.session import Base


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    platform = Column(String(100), nullable=False)  # e.g. "Amazon", "Flipkart"
    rating = Column(Float, default=4.0)
    review_count = Column(Float, default=0)
    is_verified = Column(Boolean, default=True)
    policy_summary = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    prices = relationship("ProductPrice", back_populates="seller")


class ProductPrice(Base):
    __tablename__ = "product_prices"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    product_id = Column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    seller_id = Column(String(36), ForeignKey("sellers.id", ondelete="CASCADE"), nullable=False, index=True)
    
    current_price = Column(Float, nullable=False, index=True)
    original_price = Column(Float, nullable=True)
    discount_percentage = Column(Float, default=0.0)
    currency = Column(String(10), default="INR")
    availability = Column(String(50), default="In Stock", index=True)  # "In Stock", "Out of Stock", "Limited"
    shipping_cost = Column(Float, default=0.0)
    estimated_delivery_days = Column(String(50), default="2-4 business days")
    
    last_updated = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    product = relationship("Product", back_populates="prices")
    seller = relationship("Seller", back_populates="prices")


class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    product_id = Column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    price = Column(Float, nullable=False)
    currency = Column(String(10), default="INR")
    recorded_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    source = Column(String(100), nullable=True)
