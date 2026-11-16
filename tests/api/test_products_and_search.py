import pytest
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.database.session import init_db
from backend.app.database.seed import seed_database


@pytest.mark.asyncio
async def test_products_search_and_comparison_apis():
    await init_db()
    await seed_database()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. Product list
        list_res = await client.get("/api/v1/products")
        assert list_res.status_code == 200
        products = list_res.json()
        assert len(products) >= 3

        # 2. Product detail with valid ID
        prod_id = products[0]["id"]
        detail_res = await client.get(f"/api/v1/products/{prod_id}")
        assert detail_res.status_code == 200
        detail = detail_res.json()
        assert detail["id"] == prod_id
        assert "prices" in detail
        assert "price_history" in detail
        assert "specs" in detail

        # 3. Product detail with invalid ID (Error handling)
        invalid_res = await client.get("/api/v1/products/invalid_non_existent_id_999")
        assert invalid_res.status_code == 404

        # 4. Compare products API
        compare_res = await client.post("/api/v1/compare", json={
            "product_ids": [products[0]["id"], products[1]["id"]]
        })
        assert compare_res.status_code == 200
        comp = compare_res.json()
        assert "comparison_matrix" in comp
        assert "highlights" in comp
        assert len(comp["products"]) == 2

        # 5. Price history API
        hist_res = await client.get(f"/api/v1/prices/{prod_id}/history")
        assert hist_res.status_code == 200
        hist_data = hist_res.json()
        assert "history" in hist_data
        assert "price_insight" in hist_data

        # 6. Review analysis API
        rev_res = await client.get(f"/api/v1/reviews/{prod_id}/analysis")
        assert rev_res.status_code == 200
        rev_data = rev_res.json()
        assert "sentiment_positive_pct" in rev_data
        assert "positive_themes" in rev_data
        assert "important_warnings" in rev_data
