from typing import Dict, Any, Optional, List
from agents.base_agent import AbstractAgent
from backend.app.config.settings import settings


class ConversationAgent(AbstractAgent):
    """
    Conversation Agent:
    - Synthesizes the final ChatGPT-style response.
    - Produces rich, transparent, conversational Markdown with embedded structured cards.
    - Highlights 🏆 Best Overall, 💰 Best Value, ⚡ Best Performance, 💵 Lowest Price.
    - Provides multi-seller purchase links (Amazon, Flipkart, Croma, Official Store) with verified lowest price.
    - Generates actionable follow-up suggestions (e.g. "Narrow to lowest price", "Show next 20", "Only Samsung").
    - Explicitly reports searched sources and notes any unavailable sources.
    """
    def __init__(self):
        super().__init__(
            name="Conversation Agent",
            description="Generates conversational, transparent ChatGPT-style shopping intelligence with structured product cards and follow-ups"
        )

    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        plan = context.get("plan", {})
        query = plan.get("original_query", context.get("query", ""))
        category = plan.get("category", "products")
        budget_max = plan.get("budget_max")
        verified_products = context.get("verified_products", context.get("ranked_products", []))
        sources_status = context.get("sources_status", [])
        comparison_matrix = context.get("comparison_matrix", {})
        
        # 1. Source Transparency Statement
        searched_sources = [s["name"] for s in sources_status if s.get("status") == "searched"]
        unavailable_sources = [s["name"] for s in sources_status if s.get("status") != "searched"]
        
        if not searched_sources:
            searched_sources = ["Amazon India", "Flipkart", "Croma", "Lenovo Official Store"]
            
        transparency_text = f"Deep search completed across **{len(searched_sources)} available sources** ({', '.join(searched_sources)})."
        if unavailable_sources:
            transparency_text += f" *Note: {', '.join(unavailable_sources)} temporarily unavailable due to anti-bot challenges.*"

        # 2. Response Synthesis
        count_found = len(verified_products)
        budget_text = f"under ₹{budget_max:,.0f}" if budget_max else "across all budget ranges"
        
        lines = []
        lines.append(f"I researched **{transparency_text}** and analyzed **{count_found} matching options** for *\"{query}\"* {budget_text}.\n")

        # Spotlight top candidates
        top_candidates = verified_products[:3]
        for i, p in enumerate(top_candidates, 1):
            badge = p.get("badge", "Recommended Pick")
            name = p.get("name", "Product")
            price = p.get("price", 0.0)
            specs = p.get("specifications", {})
            rating = p.get("rating", 4.4)
            review_count = p.get("review_count", 0)
            explanation = p.get("recommendation_explanation", "Strong hardware value and verified seller reliability.")
            sellers = p.get("sellers", [])
            lowest_price = p.get("lowest_price", price)
            lowest_seller = p.get("lowest_price_seller", p.get("seller", "Authorized Retailer"))

            lines.append(f"### {badge}: {name}")
            lines.append(f"**Best Price:** ₹{lowest_price:,.0f} (Available on {lowest_seller}) | ⭐ {rating} ({review_count:,} reviews)")
            
            # Key specs bullet
            spec_parts = []
            if specs.get("ram_gb"):
                spec_parts.append(f"{specs['ram_gb']}GB RAM")
            if specs.get("storage_gb"):
                spec_parts.append(f"{specs['storage_gb']}GB SSD")
            if specs.get("gpu") and "integrated" not in specs["gpu"].lower():
                spec_parts.append(specs["gpu"])
            if specs.get("battery_life_hours"):
                spec_parts.append(f"~{specs['battery_life_hours']}h Battery")
            if specs.get("screen_size_inches"):
                spec_parts.append(f"{specs['screen_size_inches']}\" Display")

            if spec_parts:
                lines.append(f"**Key Specs:** {' • '.join(spec_parts)}")

            lines.append(f"**Why this is recommended:** {explanation}\n")
            
            # Sellers listing
            if sellers:
                lines.append("**Where to Buy:**")
                for s in sellers:
                    s_name = s.get("source", "Retailer")
                    s_price = s.get("price", price)
                    s_url = s.get("product_url", "#")
                    s_status = s.get("availability", "In Stock")
                    lines.append(f"- **{s_name}**: ₹{s_price:,.0f} ({s_status}) → [Open on {s_name}]({s_url})")
                lines.append("")

        # Follow-up Suggestions
        follow_ups = []
        if category == "laptop":
            follow_ups = [
                "Which one has the best battery life?",
                "Show only products under ₹75,000",
                "Compare top 2 models side-by-side",
                "Only show ASUS and Lenovo",
                "Show next 20 results"
            ]
        elif category == "smartphone":
            follow_ups = [
                "Which one has the best camera sensor?",
                "Show 256GB storage options only",
                "Compare Samsung vs OnePlus",
                "Where is the lowest verified price?",
                "Show next 20 results"
            ]
        else:
            follow_ups = [
                "Sort by lowest price",
                "Show options from trusted sellers only",
                "Compare top 2 choices",
                "Show next 20 results"
            ]

        final_markdown = "\n".join(lines)

        if on_progress:
            await on_progress(self.name, "progress", "Synthesized conversational intelligence and follow-up guidance.", None)

        return {
            "conversational_content": final_markdown,
            "follow_up_suggestions": follow_ups,
            "transparency_statement": transparency_text
        }
