from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime


class AgentTaskResponse(BaseModel):
    id: str
    session_id: str
    agent_name: str
    status: str
    task_description: Optional[str] = None
    execution_time_ms: int = 0
    token_usage: int = 0
    error_message: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ToolCallResponse(BaseModel):
    id: str
    task_id: str
    tool_name: str
    arguments: Optional[Dict[str, Any]] = None
    result: Optional[Dict[str, Any]] = None
    latency_ms: int = 0
    status: str
    error_message: Optional[str] = None
    called_at: datetime

    class Config:
        from_attributes = True
