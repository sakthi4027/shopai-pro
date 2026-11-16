from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime


class SearchQueryRequest(BaseModel):
    query: str
    custom_budget_max: Optional[float] = None
    preferred_brands: Optional[List[str]] = None
    session_id: Optional[str] = None


class SearchSessionResponse(BaseModel):
    id: str
    user_id: str
    title: Optional[str] = None
    status: str
    created_at: datetime
    request_id: Optional[str] = None

    class Config:
        from_attributes = True


class LiveAgentEvent(BaseModel):
    session_id: str
    agent_name: str
    status: str  # "started", "progress", "completed", "warning", "error"
    message: str
    step_index: int
    total_steps: int = 10
    timestamp: datetime = datetime.utcnow()
    payload: Optional[Dict[str, Any]] = None
