from typing import Optional, List
from pydantic import BaseModel


class PreferenceUpdate(BaseModel):
    preferred_brands: Optional[List[str]] = None
    budget_max: Optional[float] = None
    preferred_ram: Optional[str] = None
    preferred_storage: Optional[str] = None
    avoid_refurbished: Optional[bool] = None
    excluded_keywords: Optional[List[str]] = None
    currency: Optional[str] = "INR"


class PreferenceResponse(BaseModel):
    id: str
    user_id: str
    preferred_brands: List[str] = []
    budget_max: Optional[float] = None
    preferred_ram: Optional[str] = None
    preferred_storage: Optional[str] = None
    avoid_refurbished: bool = True
    excluded_keywords: List[str] = []
    currency: str = "INR"

    class Config:
        from_attributes = True
