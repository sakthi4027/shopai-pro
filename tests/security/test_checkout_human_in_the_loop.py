import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.database.session import init_db
from backend.app.database.seed import seed_database


@pytest.mark.asyncio
async def test_human_in_the_loop_checkout_safety():
    await init_db()
    await seed_database()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Register test user
        email = f"buyer_{uuid.uuid4().hex[:6]}@example.com"
        reg_res = await client.post("/api/v1/auth/register", json={
            "email": email, "password": "SafePassword123!", "full_name": "Test Buyer"
        })
        token = reg_res.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # 1. Step 1: Pre-checkout review manifest
        review_res = await client.post("/api/v1/checkout/review", headers=headers, json={
            "product_id": "prod_lenovo_legion_slim5"
        })
        assert review_res.status_code == 200
        manifest = review_res.json()
        assert manifest["human_confirmation_required"] is True
        assert manifest["total_cost"] == 79990.0
        assert "HUMAN CONFIRMATION REQUIRED" in manifest["security_warning"]

        # 2. Step 2A: Explicit Human Cancellation
        cancel_res = await client.post("/api/v1/checkout/confirm", headers=headers, json={
            "product_id": "prod_lenovo_legion_slim5",
            "seller_id": manifest["seller_id"],
            "total_amount": manifest["total_cost"],
            "user_confirmed": False,
            "user_notes": "Cancelled by user before payment"
        })
        assert cancel_res.status_code == 200
        cancel_data = cancel_res.json()
        assert cancel_data["status"] == "CANCELLED"
        assert cancel_data["external_checkout_url"] is None

        # 3. Step 2B: Explicit Human Approval
        confirm_res = await client.post("/api/v1/checkout/confirm", headers=headers, json={
            "product_id": "prod_lenovo_legion_slim5",
            "seller_id": manifest["seller_id"],
            "total_amount": manifest["total_cost"],
            "user_confirmed": True
        })
        assert confirm_res.status_code == 200
        confirm_data = confirm_res.json()
        assert confirm_data["status"] == "APPROVED_READY_FOR_REDIRECT"
        assert confirm_data["external_checkout_url"] is not None
        assert confirm_data["audit_logged"] is True

        # 4. Verify Audit Log recorded both events
        audit_res = await client.get("/api/v1/audit", headers=headers)
        assert audit_res.status_code == 200
        logs = audit_res.json()
        actions = [l["action"] for l in logs]
        assert "CHECKOUT_REVIEW_GENERATED" in actions
        assert "CHECKOUT_CANCELLED_BY_USER" in actions
        assert "CHECKOUT_APPROVED_BY_USER" in actions
