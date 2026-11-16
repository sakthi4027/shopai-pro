import pytest
from agents.recommendation.agent import RecommendationAgent


@pytest.mark.asyncio
async def test_multi_factor_recommendation_ranking():
    rec_agent = RecommendationAgent()
    context = {
        "plan": {
            "budget_max": 80000.0,
            "required_features": ["32GB RAM", "1TB SSD", "RTX GPU"]
        },
        "budget_annotated_products": [
            {
                "name": "Laptop A (Strong Match, Within Budget)",
                "price": 79990.0,
                "rating": 4.6,
                "availability": "In Stock",
                "budget_status": "Within Budget",
                "trust_score": 1.0,
                "specifications": {
                    "ram_gb": 32, "storage_gb": 1024, "gpu": "RTX 4060", "cpu": "Ryzen 7", "battery_life_hours": 8.0, "warranty_months": 24
                }
            },
            {
                "name": "Laptop B (16GB RAM, Lower Specs)",
                "price": 68990.0,
                "rating": 4.2,
                "availability": "In Stock",
                "budget_status": "Within Budget",
                "trust_score": 0.95,
                "specifications": {
                    "ram_gb": 16, "storage_gb": 512, "gpu": "RTX 4050", "cpu": "Intel i5", "battery_life_hours": 5.0, "warranty_months": 12
                }
            }
        ]
    }

    res = await rec_agent.run(context)
    ranked = res.data["ranked_products"]

    assert len(ranked) == 2
    # Laptop A should be top recommendation with Best Overall badge
    top = ranked[0]
    assert "Laptop A" in top["name"]
    assert top["badge"] == "Best Overall"
    assert top["score_overall"] > ranked[1]["score_overall"]
    assert "RTX 4060" in top["recommendation_explanation"]
