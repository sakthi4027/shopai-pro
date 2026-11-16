import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from backend.app.database.session import Base


class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    
    # User memory & constraints
    preferred_brands = Column(JSON, default=list)  # e.g. ["Lenovo", "ASUS", "Apple"]
    budget_max = Column(Float, nullable=True)
    preferred_ram = Column(String(50), nullable=True)  # e.g. "32GB"
    preferred_storage = Column(String(50), nullable=True)  # e.g. "1TB"
    avoid_refurbished = Column(Boolean, default=True)
    excluded_keywords = Column(JSON, default=list)
    currency = Column(String(10), default="INR")
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="preferences")
