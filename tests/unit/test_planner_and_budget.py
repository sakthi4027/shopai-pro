import pytest
from agents.planner.agent import ShoppingPlannerAgent
from agents.budget.agent import BudgetAgent
from agents.trust.agent import ProductTrustAgent


@pytest.mark.asyncio
async def test_shopping_planner_extraction():
    planner = ShoppingPlannerAgent()
    context = {
        "query": "Find me a laptop under ₹80,000 with 32GB RAM, 1TB SSD, good battery life, and suitable for AI development.",
        "user_preferences": {"preferred_brands": ["Lenovo", "ASUS"]}
    }
    res = await planner.run(context)
    data = res.data

    assert data["category"] == "laptop"
    assert data["budget_max"] == 80000.0
    assert any("32GB" in rf for rf in data["required_features"])
    assert any("1TB" in rf for rf in data["required_features"])
    assert any("GPU" in rf or "CUDA" in rf for rf in data["required_features"])
    assert "Lenovo" in data["preferred_brands"]


@pytest.mark.asyncio
async def test_budget_agent_classification():
    budget_agent = BudgetAgent()
    context = {
        "plan": {"budget_max": 80000.0},
        "verified_products": [
            {"name": "Laptop A", "price": 74999.0},
            {"name": "Laptop B", "price": 84000.0},
            {"name": "Laptop C", "price": 99000.0}
        ]
    }
    res = await budget_agent.run(context)
    data = res.data

    within = [p["name"] for p in data["within_budget"]]
    near = [p["name"] for p in data["near_budget"]]
    over = [p["name"] for p in data["over_budget"]]

    assert "Laptop A" in within
    assert "Laptop B" in near
    assert "Laptop C" in over


@pytest.mark.asyncio
async def test_trust_agent_flags_suspicious():
    trust_agent = ProductTrustAgent()
    context = {
        "extracted_products": [
            {
                "name": "Legitimate Laptop",
                "price": 79990.0,
                "original_price": 89990.0,
                "brand": "Lenovo",
                "seller": "Authorized Store",
                "specifications": {"ram_gb": 32, "storage_gb": 1024, "cpu": "Ryzen 7", "gpu": "RTX 4060", "warranty_months": 24}
            },
            {
                "name": "Deceptive Fake Deal",
                "price": 19999.0,  # Suspiciously low for RTX 4090
                "original_price": 199000.0,
                "brand": "Unknown",
                "seller": "Unverified seller",
                "specifications": {"ram_gb": 32, "storage_gb": 2048, "gpu": "RTX 4090", "warranty_months": 0}
            }
        ]
    }
    res = await trust_agent.run(context)
    data = res.data

    assert len(data["verified_products"]) == 1
    assert data["verified_products"][0]["name"] == "Legitimate Laptop"
    assert len(data["flagged_products"]) == 1
    assert data["flagged_products"][0]["name"] == "Deceptive Fake Deal"
    assert "⚠️" in data["flagged_products"][0]["trust_warnings"][0]
