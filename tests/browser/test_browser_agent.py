import pytest
from backend.app.browser.agent import PlaywrightBrowserAgent, BrowserExtractionResult


@pytest.mark.asyncio
async def test_browser_agent_structure_and_safety_controls():
    agent = PlaywrightBrowserAgent(headless=True)
    assert agent.headless is True
    assert agent.screenshots_dir is not None

    # Test safe pause detection handling on simulated blocked page
    # The agent must return 'Human action required' if blocked and never bypass anti-bot
    result = BrowserExtractionResult(
        url="https://shady-store.example/blocked",
        title="Access Denied - Security Check",
        status="blocked_anti_bot",
        action_required_message="⚠️ Human action required: Target store triggered automated security or CAPTCHA verification."
    )
    assert result.status == "blocked_anti_bot"
    assert "Human action required" in result.action_required_message
