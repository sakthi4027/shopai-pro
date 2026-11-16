from typing import Dict, Any, Optional, List
from agents.base_agent import AbstractAgent


class ProductComparisonAgent(AbstractAgent):
    """
    Builds structured side-by-side comparison tables across hardware specifications,
    prices, battery endurance, warranty, and seller reliability.
    Identifies standout winners for Best Value, Best Performance, Cheapest Suitable,
    Best Rated, and Best Overall.
    """
    def __init__(self):
        super().__init__(
            name="Product Comparison Agent",
            description="Generates side-by-side feature comparisons and evaluates category winners"
        )

    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        products = context.get("budget_annotated_products", [])
        if not products:
            return {"comparison_matrix": [], "highlights": {}}

        # Features to compare
        features = [
            {"key": "price", "label": "Price (INR)", "formatter": lambda p: f"₹{p.get('price', 0):,.0f}"},
            {"key": "ram", "label": "RAM", "formatter": lambda p: f"{p.get('specifications', {}).get('ram_gb', 0)}GB DDR5"},
            {"key": "storage", "label": "Storage (SSD)", "formatter": lambda p: f"{p.get('specifications', {}).get('storage_gb', 0)}GB NVMe"},
            {"key": "cpu", "label": "Processor (CPU)", "formatter": lambda p: p.get('specifications', {}).get('cpu', 'N/A')},
            {"key": "gpu", "label": "Graphics (GPU)", "formatter": lambda p: p.get('specifications', {}).get('gpu', 'N/A')},
            {"key": "screen", "label": "Display", "formatter": lambda p: f"{p.get('specifications', {}).get('screen_size_inches', 0)}\""},
            {"key": "battery", "label": "Battery Life", "formatter": lambda p: f"~{p.get('specifications', {}).get('battery_life_hours', 0)} Hours"},
            {"key": "rating", "label": "User Rating", "formatter": lambda p: f"⭐ {p.get('rating', 0)} ({p.get('review_count', 0)} reviews)"},
            {"key": "warranty", "label": "Warranty", "formatter": lambda p: p.get('warranty', '12 Months')},
            {"key": "seller", "label": "Primary Seller", "formatter": lambda p: p.get('seller', 'Authorized')},
            {"key": "trust", "label": "Safety / Trust", "formatter": lambda p: f"{(p.get('trust_score', 1.0) * 100):.0f}% Verified"}
        ]

        matrix = []
        for feat in features:
            row = {"feature": feat["label"], "key": feat["key"], "values": {}}
            for p in products:
                row["values"][p["product_url"]] = feat["formatter"](p)
            matrix.append(row)

        # Highlight winners
        best_rated = max(products, key=lambda x: x.get("rating", 0.0))
        cheapest = min(products, key=lambda x: x.get("price", float("inf")))
        
        # Best performance: highest ram + best gpu
        def perf_score(p):
            ram = p.get("specifications", {}).get("ram_gb", 0)
            gpu = p.get("specifications", {}).get("gpu", "")
            gpu_weight = 40 if "4060" in gpu else (25 if "4050" in gpu else 10)
            return ram + gpu_weight

        best_perf = max(products, key=perf_score)

        # Best value: performance / price
        def value_score(p):
            perf = perf_score(p)
            price = p.get("price", 1.0)
            return (perf / price) * 100000

        best_value = max(products, key=value_score)

        highlights = {
            "best_rated": best_rated.get("name"),
            "cheapest_suitable": cheapest.get("name"),
            "best_performance": best_perf.get("name"),
            "best_value": best_value.get("name"),
            "best_overall": best_perf.get("name")  # Will be refined by Recommendation Agent
        }

        if on_progress:
            await on_progress(self.name, "progress", f"Built comparative spec matrix for {len(products)} products.", None)

        return {
            "comparison_matrix": matrix,
            "highlights": highlights
        }
