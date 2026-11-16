import asyncio
import logging
import os
from typing import Dict, Any, Optional
from pydantic import BaseModel

logger = logging.getLogger("browser_agent")


class BrowserExtractionResult(BaseModel):
    url: str
    title: str
    status: str  # "success", "blocked_anti_bot", "failed", "timeout"
    html_snippet: Optional[str] = None
    extracted_text: Optional[str] = None
    screenshot_path: Optional[str] = None
    action_required_message: Optional[str] = None


class PlaywrightBrowserAgent:
    """
    Playwright-powered Browser Automation Agent that adheres strictly to security rules:
    - Zero CAPTCHA or Anti-bot bypass: detects challenges immediately and yields 'Human action required'.
    - Headless browser navigation with state verification and screenshot capture.
    - Zero payment credential entry or storage.
    """
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.screenshots_dir = os.path.join(os.getcwd(), "browser_screenshots")
        os.makedirs(self.screenshots_dir, exist_ok=True)

    async def fetch_product_page(self, url: str) -> BrowserExtractionResult:
        try:
            from playwright.async_api import async_playwright
        except ImportError:
            return BrowserExtractionResult(
                url=url,
                title="",
                status="failed",
                action_required_message="Playwright is not installed in current environment."
            )

        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=self.headless)
                context = await browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
                page = await context.new_page()

                try:
                    response = await page.goto(url, wait_until="domcontentloaded", timeout=12000)
                except Exception as e:
                    await browser.close()
                    return BrowserExtractionResult(
                        url=url,
                        title="",
                        status="failed",
                        action_required_message=f"Navigation failed: {str(e)}"
                    )

                page_title = await page.title()
                content = await page.content()
                
                # Check for anti-bot / Cloudflare / CAPTCHA gates
                bot_signals = [
                    "captcha", 
                    "challenge-running", 
                    "verify you are human", 
                    "access denied", 
                    "blocked", 
                    "robot check", 
                    "cloudflare"
                ]
                content_lower = content.lower()
                if any(signal in content_lower for signal in bot_signals) and "product" not in page_title.lower():
                    # Save diagnostic screenshot
                    screenshot_name = f"blocked_{abs(hash(url)) % 100000}.png"
                    screenshot_path = os.path.join(self.screenshots_dir, screenshot_name)
                    try:
                        await page.screenshot(path=screenshot_path)
                    except Exception:
                        screenshot_path = None

                    await browser.close()
                    return BrowserExtractionResult(
                        url=url,
                        title=page_title,
                        status="blocked_anti_bot",
                        screenshot_path=screenshot_path,
                        action_required_message="⚠️ Human action required: Target store triggered automated security or CAPTCHA verification."
                    )

                # Page was fetched cleanly
                text_content = await page.evaluate("() => document.body.innerText")
                screenshot_name = f"page_{abs(hash(url)) % 100000}.png"
                screenshot_path = os.path.join(self.screenshots_dir, screenshot_name)
                try:
                    await page.screenshot(path=screenshot_path)
                except Exception:
                    screenshot_path = None

                await browser.close()
                return BrowserExtractionResult(
                    url=url,
                    title=page_title,
                    status="success",
                    html_snippet=content[:5000],
                    extracted_text=text_content[:3000],
                    screenshot_path=screenshot_path
                )

        except Exception as ex:
            return BrowserExtractionResult(
                url=url,
                title="",
                status="failed",
                action_required_message=f"Browser agent error: {str(ex)}"
            )


browser_agent = PlaywrightBrowserAgent()
