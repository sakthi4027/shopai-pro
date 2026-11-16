# Security, Human-in-the-Loop & Privacy Architecture

## Strict Zero-Autonomous-Purchase Guarantee
The AI assistant is architecturally restricted from executing payments or financial transactions automatically:
1. When a user requests to purchase an item, the system generates an itemized pre-checkout manifest.
2. The user must review product name, seller, base price, tax, and total before clicking `[Confirm]`.
3. If the user clicks `[Cancel]`, the transaction immediately aborts.
4. If the user clicks `[Confirm]`, the assistant redirects the user to the merchant's authorized official payment portal.
5. Credit card numbers, CVVs, and banking credentials are never requested, transmitted, or stored.

## Isolated User Workspaces
- All search sessions, shopping memories, saved items, and price alerts are scoped strictly to the authenticated `user_id`.
- The authorization dependency extracts the caller's identity directly from the cryptographically verified JWT token, preventing Insecure Direct Object Reference (IDOR) attacks.

## Safe Web Automation
- The Playwright browser agent operates with anti-bot detection safeguards.
- When an e-commerce website triggers a CAPTCHA or Cloudflare challenge, the agent halts and yields `Human action required` rather than attempting forbidden bypasses.
