from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict, Field


class CreateConversationRequest(BaseModel):
    title: Optional[str] = None
    search_mode: str = "deep"  # "quick", "deep", "maximum"


class SendMessageRequest(BaseModel):
    content: str = Field(..., min_length=1, description="Natural-language shopping query or follow-up")
    search_mode: Optional[str] = "deep"
    request_id: Optional[str] = None


class MessageResponse(BaseModel):
    id: str
    conversation_id: str
    role: str  # "user", "assistant", "system"
    content: str
    request_id: Optional[str] = None
    agent_steps: List[Dict[str, Any]] = []
    sources_status: List[Dict[str, Any]] = []
    products_payload: List[Dict[str, Any]] = []
    total_products_found: int = 0
    comparison_payload: Dict[str, Any] = {}
    follow_up_suggestions: List[str] = []
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ConversationSummaryResponse(BaseModel):
    id: str
    title: str
    search_mode: str
    created_at: datetime
    updated_at: datetime
    message_count: int = 0

    model_config = ConfigDict(from_attributes=True)


class ConversationDetailResponse(BaseModel):
    id: str
    title: str
    search_mode: str
    active_constraints: Dict[str, Any] = {}
    created_at: datetime
    updated_at: datetime
    messages: List[MessageResponse] = []

    model_config = ConfigDict(from_attributes=True)


class CheckoutIntentRequest(BaseModel):
    product_id: Optional[str] = None
    product_name: str
    seller_name: str
    price: float
    shipping_cost: float = 0.0
    product_url: str


class CheckoutManifestResponse(BaseModel):
    confirmation_required: bool = True
    notice: str = "⚠️ HUMAN CONFIRMATION REQUIRED BEFORE PURCHASE ASSISTANCE"
    product_name: str
    price: float
    seller_name: str
    shipping_cost: float
    total_cost: float
    currency: str = "INR"
    checkout_url: str
    security_guarantee: str = "Strict zero-autonomous-purchase guarantee. We never store credit card or payment information."
