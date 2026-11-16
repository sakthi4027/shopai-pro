import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.database.session import init_db


@pytest.mark.asyncio
async def test_auth_registration_login_and_isolation():
    await init_db()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. Register User A
        email_a = f"user_a_{uuid.uuid4().hex[:6]}@example.com"
        res_a = await client.post("/api/v1/auth/register", json={
            "email": email_a,
            "password": "Password123!",
            "full_name": "User Alpha"
        })
        assert res_a.status_code == 200
        token_a = res_a.json()["access_token"]
        headers_a = {"Authorization": f"Bearer {token_a}"}

        # 2. Register User B
        email_b = f"user_b_{uuid.uuid4().hex[:6]}@example.com"
        res_b = await client.post("/api/v1/auth/register", json={
            "email": email_b,
            "password": "Password123!",
            "full_name": "User Beta"
        })
        assert res_b.status_code == 200
        token_b = res_b.json()["access_token"]
        headers_b = {"Authorization": f"Bearer {token_b}"}

        # 3. User A configures custom shopping memory
        update_res_a = await client.put("/api/v1/preferences", headers=headers_a, json={
            "preferred_brands": ["Lenovo"],
            "budget_max": 85000.0,
            "preferred_ram": "32GB"
        })
        assert update_res_a.status_code == 200
        pref_a = update_res_a.json()
        assert pref_a["preferred_brands"] == ["Lenovo"]
        assert pref_a["budget_max"] == 85000.0

        # 4. Strict Isolation: Verify User B's preferences are completely distinct from User A
        get_res_b = await client.get("/api/v1/preferences", headers=headers_b)
        assert get_res_b.status_code == 200
        pref_b = get_res_b.json()
        assert pref_b["user_id"] != pref_a["user_id"]
        assert pref_b["budget_max"] is None  # User B has not set budget

        # 5. User A creates price alert for a product
        alert_res_a = await client.post("/api/v1/alerts", headers=headers_a, json={
            "product_id": "prod_lenovo_legion_slim5",
            "target_price": 75000.0
        })
        assert alert_res_a.status_code == 200

        # User A sees 1 alert
        alerts_list_a = await client.get("/api/v1/alerts", headers=headers_a)
        assert len(alerts_list_a.json()) == 1

        # Strict Isolation: User B sees 0 alerts
        alerts_list_b = await client.get("/api/v1/alerts", headers=headers_b)
        assert len(alerts_list_b.json()) == 0
