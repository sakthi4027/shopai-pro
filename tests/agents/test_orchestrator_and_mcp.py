import pytest
from mcp.servers.ecommerce_server import mcp_server
from backend.app.database.session import init_db
from backend.app.database.seed import seed_database


@pytest.mark.asyncio
async def test_all_10_mcp_tools():
    await init_db()
    await seed_database()

    # 1. Verify 10 tools are registered
    tools = mcp_server.list_tools()
    assert len(tools) == 10
    tool_names = [t["name"] for t in tools]
    expected_tools = [
        "product_search",
        "product_details",
        "price_lookup",
        "review_search",
        "seller_lookup",
        "availability_check",
        "product_compare",
        "price_history",
        "shopping_preferences",
        "notification_service"
    ]
    for et in expected_tools:
        assert et in tool_names

    # 2. Test tool execution with schema validation
    # product_search tool
    res_search = await mcp_server.call_tool("product_search", {"query": "laptop", "limit": 3})
    assert res_search.status == "success"
    assert res_search.data["total_found"] > 0

    # price_lookup tool
    res_price = await mcp_server.call_tool("price_lookup", {"product_id": "prod_lenovo_legion_slim5"})
    assert res_price.status == "success"
    assert res_price.data["best_price"] > 0

    # 3. Test Permission Validation: shopping_preferences requires user_id in user_context
    res_unauth = await mcp_server.call_tool("shopping_preferences", {"action": "get"}, user_context=None)
    assert res_unauth.status == "permission_denied"

    # Authenticated user context succeeds
    res_auth = await mcp_server.call_tool(
        "shopping_preferences",
        {"action": "get"},
        user_context={"user_id": "u_demo_user_001", "role": "user"}
    )
    assert res_auth.status == "success"
    assert res_auth.data["user_id"] == "u_demo_user_001"
