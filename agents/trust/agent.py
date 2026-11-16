from typing import Dict, Any, Optional, List
from agents.base_agent import AbstractAgent


class ProductTrustAgent(AbstractAgent):
    """
    Evaluates seller and product authenticity, flags suspicious price discrepancies,
    missing warranty terms, conflicting specifications, and unverified merchant claims.
    """
    def __init__(self):
        super().__init__(
            name="Product Safety / Trust Agent",
            description="Audits product claims, warranty clarity, seller repute, and flags deceptive listings"
        )

    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        extracted_data = context.get("extracted_products", [])
        verified_items = []
        flagged_items = []

        for p in extracted_data:
            warnings = []
            trust_score = 1.0  # Out of 1.0
            
            price = p.get("price", 0.0)
            orig_price = p.get("original_price", price)
            specs = p.get("specifications", {})
            seller = p.get("seller", "")
            brand = p.get("brand", "")

            # 1. Suspiciously low price detection (e.g. claiming RTX 4090 or 32GB RAM under ₹30,000)
            if price < 35000 and ("RTX" in str(specs.get("gpu", "")) or specs.get("ram_gb", 0) >= 32):
                trust_score -= 0.5
                warnings.append("⚠️ Suspiciously low price for advertised flagship hardware. High risk of counterfeit or misrepresented components.")

            # 2. Extreme discount claim check (> 75% discount is often a bait-and-switch)
            if orig_price > 0 and ((orig_price - price) / orig_price) > 0.70:
                trust_score -= 0.2
                warnings.append("⚠️ Excessive discount claim (>70% off) could indicate artificial MSRP inflation or bait-and-switch pricing.")

            # 3. Missing or zero warranty
            if specs.get("warranty_months", 0) <= 0:
                trust_score -= 0.25
                warnings.append("⚠️ No official manufacturer warranty declared or unclear warranty terms.")

            # 4. Unverified Seller / Shady domain
            if "unverified" in seller.lower() or "shady" in p.get("product_url", "").lower() or brand.lower() in ["generic/unknown", "unknown"]:
                trust_score -= 0.4
                warnings.append("⚠️ Seller or manufacturer is unverified. ⚠️ Information could not be independently verified.")

            # 5. Missing critical specifications
            if not specs.get("cpu") or not specs.get("ram_gb"):
                trust_score -= 0.2
                warnings.append("⚠️ Key hardware specifications are missing from the listing.")

            trust_score = max(0.0, min(1.0, round(trust_score, 2)))
            p_copy = dict(p)
            p_copy["trust_score"] = trust_score
            p_copy["trust_warnings"] = warnings
            p_copy["is_safe"] = trust_score >= 0.70

            if trust_score >= 0.70:
                verified_items.append(p_copy)
            else:
                flagged_items.append(p_copy)

        if on_progress:
            await on_progress(self.name, "progress", f"Audited {len(extracted_data)} items: {len(verified_items)} verified, {len(flagged_items)} flagged for safety risks.", None)

        return {
            "verified_products": verified_items,
            "flagged_products": flagged_items
        }
