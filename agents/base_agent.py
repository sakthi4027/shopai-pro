import time
import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from pydantic import BaseModel

logger = logging.getLogger("agents")


class AgentExecutionResult(BaseModel):
    agent_name: str
    status: str  # "completed", "warning", "failed"
    execution_time_ms: int
    data: Dict[str, Any]
    warnings: List[str] = []
    error: Optional[str] = None


class AbstractAgent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    async def run(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> AgentExecutionResult:
        start_time = time.time()
        try:
            if on_progress:
                await on_progress(self.name, "started", f"{self.name} started execution", None)
            
            result_data = await self._execute(context, on_progress)
            
            latency = int((time.time() - start_time) * 1000)
            if on_progress:
                await on_progress(self.name, "completed", f"{self.name} completed successfully", result_data)

            return AgentExecutionResult(
                agent_name=self.name,
                status="completed",
                execution_time_ms=latency,
                data=result_data
            )
        except Exception as e:
            latency = int((time.time() - start_time) * 1000)
            logger.exception(f"Error in agent {self.name}: {str(e)}")
            if on_progress:
                await on_progress(self.name, "error", f"Error in {self.name}: {str(e)}", None)
            return AgentExecutionResult(
                agent_name=self.name,
                status="failed",
                execution_time_ms=latency,
                data={},
                error=str(e)
            )

    @abstractmethod
    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        pass
