import pytest
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.database.session import init_db
from backend.app.database.seed import seed_database


@pytest.mark.asyncio
async def test_conversational_deep_search_api():
    await init_db()
    await seed_database()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # 1. Register & Login User
        auth_resp = await ac.post("/api/v1/auth/login", json={
            "email": "demo@ecommerce-ai.com",
            "password": "password123"
        })
        assert auth_resp.status_code == 200
        token = auth_resp.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # 2. Create a new conversation thread
        conv_resp = await ac.post("/api/v1/conversations", json={
            "title": "AI Laptop Research Thread",
            "search_mode": "deep"
        }, headers=headers)
        assert conv_resp.status_code == 201
        conv_data = conv_resp.json()
        conv_id = conv_data["id"]
        assert conv_data["search_mode"] == "deep"

        # 3. Turn 1: Initial natural-language request
        turn1_resp = await ac.post(f"/api/v1/conversations/{conv_id}/messages", json={
            "content": "Find me a laptop under ₹80,000 with 32GB RAM, 1TB SSD, and suitable for AI development."
        }, headers=headers)
        assert turn1_resp.status_code == 200
        turn1_data = turn1_resp.json()
        assert turn1_data["role"] == "assistant"
        assert len(turn1_data["products_payload"]) > 0
        assert len(turn1_data["sources_status"]) > 0
        assert len(turn1_data["follow_up_suggestions"]) > 0
        
        # Verify first product has multi-seller intelligence & lowest price
        top_p = turn1_data["products_payload"][0]
        assert "sellers" in top_p
        assert len(top_p["sellers"]) >= 1
        assert top_p["lowest_price"] > 0
        assert "verification" in top_p
        assert top_p["verification"]["is_verified"] is True

        # 4. Turn 2: Follow-up conversational constraint refinement ("Only Lenovo")
        turn2_resp = await ac.post(f"/api/v1/conversations/{conv_id}/messages", json={
            "content": "Only Lenovo."
        }, headers=headers)
        assert turn2_resp.status_code == 200
        turn2_data = turn2_resp.json()
        # Verify multi-turn memory: active constraints carry forward
        for prod in turn2_data["products_payload"][:2]:
            assert "lenovo" in prod["name"].lower() or "lenovo" in prod.get("brand", "").lower()

        # 5. Check Conversation Detail endpoint
        detail_resp = await ac.get(f"/api/v1/conversations/{conv_id}", headers=headers)
        assert detail_resp.status_code == 200
        detail_data = detail_resp.json()
        assert len(detail_data["messages"]) == 4  # 2 user messages + 2 assistant messages
        assert detail_data["active_constraints"]["category"] == "laptop"

        # 6. Test Human-in-the-Loop Checkout Intent Gate
        checkout_resp = await ac.post("/api/v1/conversations/checkout-intent", json={
            "product_id": top_p.get("id"),
            "product_name": top_p["name"],
            "seller_name": top_p.get("lowest_price_seller", "Amazon India"),
            "price": top_p["lowest_price"],
            "shipping_cost": 0.0,
            "product_url": top_p.get("lowest_price_url", "https://www.amazon.in")
        }, headers=headers)
        assert checkout_resp.status_code == 200
        checkout_data = checkout_resp.json()
        assert checkout_data["confirmation_required"] is True
        assert checkout_data["total_cost"] == top_p["lowest_price"]
        assert "HUMAN CONFIRMATION REQUIRED" in checkout_data["notice"]

        # 7. Delete conversation
        del_resp = await ac.delete(f"/api/v1/conversations/{conv_id}", headers=headers)
        assert del_resp.status_code == 204
