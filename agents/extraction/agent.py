import datetime
from typing import Dict, Any, Optional, List
from agents.base_agent import AbstractAgent


class ProductExtractionAgent(AbstractAgent):
    """
    Extracts structured schema fields from raw product candidates:
    Product name, brand, model, price, currency, rating, review count,
    availability, specifications, seller, warranty, shipping, product URL,
    image URL, source, last checked timestamp.
    """
    def __init__(self):
        super().__init__(
            name="Product Extraction Agent",
            description="Extracts normalized structured specifications and metadata from candidate pages"
        )

    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        search_data = context.get("search_results", {})
        raw_candidates = search_data.get("products", [])

        extracted = []
        now_iso = datetime.datetime.utcnow().isoformat()

        for c in raw_candidates:
            specs = c.get("specs", {})
            item = {
                "name": c.get("raw_name"),
                "brand": c.get("brand"),
                "model": c.get("model"),
                "price": float(c.get("price", 0.0)),
                "original_price": float(c.get("original_price", c.get("price", 0.0))),
                "currency": "INR",
                "rating": float(c.get("rating", 0.0)),
                "review_count": int(c.get("review_count", 0)),
                "availability": c.get("availability", "In Stock"),
                "specifications": {
                    "ram_gb": specs.get("ram_gb"),
                    "storage_gb": specs.get("storage_gb"),
                    "cpu": specs.get("cpu"),
                    "gpu": specs.get("gpu"),
                    "screen_size_inches": specs.get("screen_size_inches"),
                    "battery_life_hours": specs.get("battery_life_hours"),
                    "weight_kg": specs.get("weight_kg"),
                    "os": specs.get("os"),
                    "warranty_months": specs.get("warranty_months", 12)
                },
                "seller": c.get("source"),
                "warranty": f"{specs.get('warranty_months', 12)} Months Official Warranty",
                "shipping": c.get("shipping", "Standard Delivery"),
                "product_url": c.get("url"),
                "url": c.get("url"),
                "image_url": c.get("image"),
                "image": c.get("image"),
                "source": c.get("source"),
                "sellers": c.get("sellers", []),
                "lowest_price": c.get("lowest_price", float(c.get("price", 0.0))),
                "lowest_price_seller": c.get("lowest_price_seller", c.get("source")),
                "lowest_price_url": c.get("lowest_price_url", c.get("url")),
                "last_checked_timestamp": now_iso
            }
            extracted.append(item)

        if on_progress:
            await on_progress(self.name, "progress", f"Extracted structured specifications across {len(extracted)} candidate products.", None)

        return {"extracted_products": extracted}
