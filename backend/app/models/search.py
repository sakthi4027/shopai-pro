import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from backend.app.database.session import Base


class SearchSession(Base):
    __tablename__ = "search_sessions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=True)
    status = Column(String(50), default="active", index=True)  # "active", "completed", "failed"
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="search_sessions")
    requests = relationship("ShoppingRequest", back_populates="session", cascade="all, delete-orphan")
    agent_tasks = relationship("AgentTask", back_populates="session", cascade="all, delete-orphan")


class ShoppingRequest(Base):
    __tablename__ = "shopping_requests"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    session_id = Column(String(36), ForeignKey("search_sessions.id", ondelete="CASCADE"), nullable=False, index=True)
    raw_query = Column(String(1000), nullable=False)
    
    # Planner Extracted fields
    category = Column(String(100), nullable=True)
    budget_max = Column(Float, nullable=True)
    required_features = Column(JSON, default=list)
    preferred_features = Column(JSON, default=list)
    optional_features = Column(JSON, default=list)
    excluded_features = Column(JSON, default=list)
    
    status = Column(String(50), default="pending", index=True)  # "pending", "in_progress", "completed", "failed"
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    session = relationship("SearchSession", back_populates="requests")
    recommendations = relationship("Recommendation", back_populates="request", cascade="all, delete-orphan")
