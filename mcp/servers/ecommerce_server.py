from typing import Dict, Any, Optional
from mcp.tools.base import BaseMCPTool, ToolExecutionResult
from mcp.tools.implementations import (
    ProductSearchTool,
    ProductDetailsTool,
    PriceLookupTool,
    ReviewSearchTool,
    SellerLookupTool,
    AvailabilityCheckTool,
    ProductCompareTool,
    PriceHistoryTool,
    ShoppingPreferencesTool,
    NotificationServiceTool,
    GetProductUrlTool,
    SearchSourceTool
)


class MCPServer:
    def __init__(self):
        self._tools: Dict[str, BaseMCPTool] = {}
        self._aliases: Dict[str, BaseMCPTool] = {}
        self._register_default_tools()

    def _register_default_tools(self):
        tools = [
            ProductSearchTool(),
            ProductDetailsTool(),
            PriceLookupTool(),
            ReviewSearchTool(),
            SellerLookupTool(),
            AvailabilityCheckTool(),
            ProductCompareTool(),
            PriceHistoryTool(),
            ShoppingPreferencesTool(),
            NotificationServiceTool()
        ]
        for t in tools:
            self._tools[t.name] = t
        
        # Extended auxiliary tools
        get_url_tool = GetProductUrlTool()
        search_source_tool = SearchSourceTool()
        self._aliases[get_url_tool.name] = get_url_tool
        self._aliases[search_source_tool.name] = search_source_tool

        # Section 28 Aliases
        self._aliases["search_products"] = self._tools["product_search"]
        self._aliases["get_product_details"] = self._tools["product_details"]
        self._aliases["compare_products"] = self._tools["product_compare"]
        self._aliases["get_price"] = self._tools["price_lookup"]
        self._aliases["get_sellers"] = self._tools["seller_lookup"]
        self._aliases["get_reviews"] = self._tools["review_search"]
        self._aliases["check_availability"] = self._tools["availability_check"]

    def get_tool(self, name: str) -> Optional[BaseMCPTool]:
        return self._tools.get(name) or self._aliases.get(name)

    def list_tools(self) -> list[dict]:
        return [
            {
                "name": t.name,
                "description": t.description,
                "input_schema": t.input_schema.model_json_schema(),
                "output_schema": t.output_schema.model_json_schema(),
                "required_role": t.required_role,
                "timeout_seconds": t.timeout_seconds
            }
            for t in self._tools.values()
        ]

    async def call_tool(
        self, 
        tool_name: str, 
        params: dict, 
        user_context: Optional[dict] = None
    ) -> ToolExecutionResult:
        tool = self.get_tool(tool_name)
        if not tool:
            return ToolExecutionResult(
                tool_name=tool_name,
                status="error",
                error=f"Tool '{tool_name}' is not registered on this MCP server"
            )
        return await tool.execute(params, user_context)


mcp_server = MCPServer()
