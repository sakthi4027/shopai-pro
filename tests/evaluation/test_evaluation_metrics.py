import pytest
from backend.app.rag.engine import rag_engine
from agents.orchestrator.agent import orchestrator_agent


def test_rag_knowledge_grounding_and_traceability():
    # 1. Query verified spec documentation
    res = rag_engine.generate_grounded_answer("Lenovo Legion Slim 5 battery life and RAM specs")
    assert res["confidence"] > 0.0
    assert len(res["citations"]) > 0
    # Traceability: every citation has title and url
    for c in res["citations"]:
        assert "http" in c["source"] or ".pdf" in c["source"]
    assert "80Wh" in res["answer"] or "RAM" in res["answer"]


def test_rag_prevents_hallucination_on_unknown():
    # Groundedness test: asking for fictional nonexistent product
    res = rag_engine.generate_grounded_answer("Fictional Quantum HyperComputer X-9000 with 1000 Terabytes")
    # Must report unknown rather than inventing facts
    assert "No verified technical documentation available" in res["answer"] or res["confidence"] < 0.10


@pytest.mark.asyncio
async def test_end_to_end_search_quality_and_spec_fulfillment():
    result = await orchestrator_agent.execute_workflow(
        query="Find me a laptop under ₹80,000 with 32GB RAM, 1TB SSD, good battery life, and suitable for AI development."
    )
    # 1. Search Quality & Reliability
    assert len(result["ranked_products"]) > 0

    # 2. Requirement Matching
    top_product = result["ranked_products"][0]
    specs = top_product["specifications"]
    assert specs["ram_gb"] >= 32
    assert specs["storage_gb"] >= 1000
    assert "4060" in specs["gpu"]
    assert top_product["price"] <= 80000.0

    # 3. Grounded Explanation
    assert len(top_product["recommendation_explanation"]) > 20
    assert "RAM" in top_product["recommendation_explanation"]
