from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class CheckoutReviewRequest(BaseModel):
    product_id: str
    seller_id: Optional[str] = None
    shipping_speed: Optional[str] = "Standard"


class CheckoutReviewResponse(BaseModel):
    product_id: str
    product_name: str
    brand: Optional[str]
    model: Optional[str]
    seller_id: str
    seller_name: str
    seller_rating: float
    base_price: float
    shipping_cost: float
    estimated_tax: float
    total_cost: float
    currency: str = "INR"
    estimated_delivery: str
    human_confirmation_required: bool = True
    security_warning: str = "⚠️ HUMAN CONFIRMATION REQUIRED: Review all details before approving. No financial transaction or payment occurs without your explicit confirmation. Card details are NEVER stored."


class CheckoutConfirmationRequest(BaseModel):
    product_id: str
    seller_id: str
    total_amount: float
    user_confirmed: bool  # Must be explicitly True
    user_notes: Optional[str] = None


class CheckoutConfirmationResponse(BaseModel):
    confirmation_id: str
    status: str  # "APPROVED_READY_FOR_REDIRECT" or "CANCELLED"
    message: str
    external_checkout_url: Optional[str] = None
    audit_logged: bool = True
