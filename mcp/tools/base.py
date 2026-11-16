import time
import asyncio
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, Type
from pydantic import BaseModel, Field


class ToolExecutionResult(BaseModel):
    tool_name: str
    status: str  # "success", "error", "timeout", "permission_denied"
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    latency_ms: int = 0


class BaseMCPTool(ABC):
    name: str
    description: str
    input_schema: Type[BaseModel]
    output_schema: Type[BaseModel]
    required_role: str = "user"  # "public", "user", "admin"
    timeout_seconds: float = 10.0

    async def execute(self, params: Dict[str, Any], user_context: Optional[Dict[str, Any]] = None) -> ToolExecutionResult:
        start_time = time.time()
        
        # 1. Permission Validation
        if self.required_role != "public":
            if not user_context or not user_context.get("user_id"):
                latency = int((time.time() - start_time) * 1000)
                return ToolExecutionResult(
                    tool_name=self.name,
                    status="permission_denied",
                    error="Authentication and user context required for this tool",
                    latency_ms=latency
                )
            if self.required_role == "admin" and user_context.get("role") != "admin":
                latency = int((time.time() - start_time) * 1000)
                return ToolExecutionResult(
                    tool_name=self.name,
                    status="permission_denied",
                    error="Admin privileges required for this tool",
                    latency_ms=latency
                )

        # 2. Input Schema Validation
        try:
            validated_input = self.input_schema(**params)
        except Exception as validation_err:
            latency = int((time.time() - start_time) * 1000)
            return ToolExecutionResult(
                tool_name=self.name,
                status="error",
                error=f"Input validation error: {str(validation_err)}",
                latency_ms=latency
            )

        # 3. Execution with Timeout
        try:
            raw_result = await asyncio.wait_for(
                self._run(validated_input, user_context),
                timeout=self.timeout_seconds
            )
            # Output Schema Validation
            validated_output = self.output_schema(**raw_result) if isinstance(raw_result, dict) else raw_result
            output_dict = validated_output.model_dump() if hasattr(validated_output, "model_dump") else raw_result
            latency = int((time.time() - start_time) * 1000)
            return ToolExecutionResult(
                tool_name=self.name,
                status="success",
                data=output_dict,
                latency_ms=latency
            )
        except asyncio.TimeoutError:
            latency = int((time.time() - start_time) * 1000)
            return ToolExecutionResult(
                tool_name=self.name,
                status="timeout",
                error=f"Tool execution timed out after {self.timeout_seconds}s",
                latency_ms=latency
            )
        except Exception as exec_err:
            latency = int((time.time() - start_time) * 1000)
            return ToolExecutionResult(
                tool_name=self.name,
                status="error",
                error=f"Tool internal execution failure: {str(exec_err)}",
                latency_ms=latency
            )

    @abstractmethod
    async def _run(self, input_data: BaseModel, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Internal execution method implemented by specialized tools"""
        pass
