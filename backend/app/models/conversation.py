import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from backend.app.database.session import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), default="New Shopping Research", nullable=False)
    search_mode = Column(String(50), default="deep", nullable=False)  # "quick", "deep", "maximum"
    active_constraints = Column(JSON, default=dict)  # Multi-turn memory: category, budget, required, excluded, brands
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan", order_by="Message.created_at")


class Message(Base):
    __tablename__ = "messages"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    conversation_id = Column(String(36), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False, index=True)
    role = Column(String(20), nullable=False)  # "user", "assistant", "system"
    content = Column(Text, nullable=False)
    
    # Detailed AI & Agent Intelligence Payloads
    agent_steps = Column(JSON, default=list)  # Step-by-step thinking traces
    sources_status = Column(JSON, default=list)  # List of sources searched with status
    products_payload = Column(JSON, default=list)  # Embedded normalized products with multi-seller arrays
    total_products_found = Column(Integer, default=0)
    comparison_payload = Column(JSON, default=dict)  # Comparison matrix
    follow_up_suggestions = Column(JSON, default=list)  # Guided follow-up refinement pills
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    conversation = relationship("Conversation", back_populates="messages")


class SearchSource(Base):
    __tablename__ = "search_sources"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    source_type = Column(String(50), default="marketplace")  # "marketplace", "retailer", "brand"
    base_url = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    health_status = Column(String(50), default="operational")  # "operational", "rate_limited", "anti_bot_challenge"
    last_checked = Column(DateTime, default=datetime.utcnow, nullable=False)
