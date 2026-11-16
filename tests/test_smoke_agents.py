import asyncio
import pytest
from agents.orchestrator.agent import orchestrator_agent


@pytest.mark.asyncio
async def test_full_agent_workflow():
    events = []
    async def log_event(agent, status, msg, payload):
        events.append((agent, status, msg))

    query = "Find me a laptop under ₹80,000 with 32GB RAM, 1TB SSD, good battery life, and suitable for AI development."
    result = await orchestrator_agent.execute_workflow(
        query=query,
        on_event=log_event
    )

    assert result is not None
    assert "plan" in result
    assert result["plan"]["category"] == "laptop"
    assert result["plan"]["budget_max"] == 80000.0
    assert len(result["ranked_products"]) > 0
    
    top = result["ranked_products"][0]
    assert "score_overall" in top
    assert "recommendation_explanation" in top
    assert len(events) >= 10
    print(f"\nWorkflow succeeded with {len(events)} events!")
    print(f"Top product: {top['name']} ({top['badge']}) - Score: {top['score_overall']}%")


if __name__ == "__main__":
    asyncio.run(test_full_agent_workflow())
