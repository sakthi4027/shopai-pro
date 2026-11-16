import httpx
from typing import Dict, Any, Optional, List
from agents.base_agent import AbstractAgent
from backend.app.config.settings import settings


class RecommendationAgent(AbstractAgent):
    """
    Computes rigorous multi-factor scoring based on:
    Requirement Match + Price + Performance + Reviews + Availability + Warranty = Recommendation Score.
    Generates transparent, grounded natural-language explanations without hallucinations.
    Never relies solely on star ratings.
    Integrates live LLM synthesis (Gemini / OpenAI) when API keys are configured in .env.
    """
    def __init__(self):
        super().__init__(
            name="Recommendation Agent",
            description="Computes multi-factor scores, ranks top candidates, and provides transparent purchase justifications"
        )

    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        plan = context.get("plan", {})
        products = context.get("budget_annotated_products", [])
        budget_max = plan.get("budget_max")
        required_features = plan.get("required_features", [])

        scored_products = []

        for p in products:
            price = p.get("price", 0.0)
            specs = p.get("specifications", {})
            rating = p.get("rating", 0.0)
            trust_score = p.get("trust_score", 1.0)
            
            # 1. Requirement Match Score (0 - 100)
            match_points = 0
            total_checks = 4
            
            # Check RAM constraint
            ram_gb = specs.get("ram_gb", 0)
            if any("32GB" in rf for rf in required_features):
                if ram_gb >= 32:
                    match_points += 1.0
                elif ram_gb >= 16:
                    match_points += 0.5
            else:
                match_points += 1.0

            # Check SSD constraint
            storage_gb = specs.get("storage_gb", 0)
            if any("1TB" in rf for rf in required_features):
                if storage_gb >= 1000:
                    match_points += 1.0
                elif storage_gb >= 500:
                    match_points += 0.5
            else:
                match_points += 1.0

            # Check GPU / AI constraint
            gpu_str = str(specs.get("gpu", "")).lower()
            if any("GPU" in rf or "RTX" in rf for rf in required_features):
                if "4060" in gpu_str:
                    match_points += 1.0
                elif "4050" in gpu_str:
                    match_points += 0.75
                elif "rtx" in gpu_str:
                    match_points += 0.6
            else:
                match_points += 1.0

            # Check Battery
            battery_hours = specs.get("battery_life_hours", 0)
            if battery_hours >= 7.0:
                match_points += 1.0
            elif battery_hours >= 5.0:
                match_points += 0.7
            else:
                match_points += 0.4

            score_match = round((match_points / total_checks) * 100, 1)

            # 2. Price Score (0 - 100)
            if budget_max and budget_max > 0:
                if price <= budget_max:
                    # Better score the closer to optimal or lower
                    saving_pct = (budget_max - price) / budget_max
                    score_price = min(100.0, 85.0 + (saving_pct * 30.0))
                else:
                    penalty_pct = (price - budget_max) / budget_max
                    score_price = max(20.0, 85.0 - (penalty_pct * 150.0))
            else:
                score_price = 85.0
            score_price = round(score_price, 1)

            # 3. Performance Score (0 - 100)
            perf_pts = 0
            if "4060" in gpu_str:
                perf_pts += 45
            elif "4050" in gpu_str:
                perf_pts += 30
            else:
                perf_pts += 15

            if ram_gb >= 32:
                perf_pts += 35
            elif ram_gb >= 16:
                perf_pts += 20
            else:
                perf_pts += 10

            cpu_str = str(specs.get("cpu", "")).lower()
            if "ryzen 7" in cpu_str or "i7" in cpu_str:
                perf_pts += 20
            else:
                perf_pts += 10
            score_performance = float(perf_pts)

            # 4. Reviews Score (0 - 100)
            score_reviews = round((rating / 5.0) * 100, 1)

            # 5. Availability & Warranty bonus
            score_avail = 100.0 if p.get("availability") == "In Stock" else 40.0
            score_warranty = 100.0 if specs.get("warranty_months", 0) >= 24 else 80.0

            # Weighted overall score:
            # Match 30%, Price 25%, Perf 20%, Reviews 15%, Trust & Warranty 10%
            score_overall = (
                (0.30 * score_match) +
                (0.25 * score_price) +
                (0.20 * score_performance) +
                (0.15 * score_reviews) +
                (0.05 * (trust_score * 100)) +
                (0.05 * score_warranty)
            )
            score_overall = round(score_overall, 1)

            # Rationale explanation generator
            reasons = []
            if score_match >= 90:
                reasons.append(f"Directly satisfies your target hardware specifications ({ram_gb}GB RAM, {storage_gb}GB SSD).")
            if p.get("budget_status") == "Within Budget":
                reasons.append(f"Comfortably within your ₹{budget_max:,.0f} budget (priced at ₹{price:,.0f}).")
            elif p.get("budget_status") == "Near Budget":
                reasons.append(f"Near budget (+{p.get('budget_note')}) with high hardware payoff.")
            if "4060" in gpu_str:
                reasons.append("Equipped with NVIDIA RTX 4060 8GB VRAM with Tensor Cores, ideal for local LLMs, CUDA acceleration, and AI fine-tuning.")
            if battery_hours >= 7.0:
                reasons.append(f"Strong real-world battery endurance (~{battery_hours} hours).")
            if specs.get("warranty_months", 0) >= 24:
                reasons.append("Includes extended 2-Year Official Manufacturer Warranty.")

            p_copy = dict(p)
            p_copy["score_overall"] = score_overall
            p_copy["score_match"] = score_match
            p_copy["score_price"] = score_price
            p_copy["score_performance"] = score_performance
            p_copy["score_reviews"] = score_reviews
            p_copy["recommendation_explanation"] = " ".join(reasons)
            scored_products.append(p_copy)

        # Sort products by score_overall descending
        scored_products.sort(key=lambda x: x["score_overall"], reverse=True)

        # Assign badges
        if scored_products:
            # 1. Best Overall = highest overall score
            scored_products[0]["badge"] = "Best Overall"

            # 2. Cheapest suitable
            cheapest = min(
                [p for p in scored_products if p.get("budget_status") in ["Within Budget", "Near Budget"]],
                key=lambda x: x["price"],
                default=None
            )
            if cheapest and cheapest != scored_products[0]:
                cheapest["badge"] = "Cheapest Suitable"

            # 3. Best Performance
            highest_perf = max(scored_products, key=lambda x: x["score_performance"])
            if highest_perf and highest_perf != scored_products[0] and not highest_perf.get("badge"):
                highest_perf["badge"] = "Best Performance"

            # 4. Best Value
            best_val = max(
                [p for p in scored_products if p.get("budget_status") == "Within Budget"],
                key=lambda x: (x["score_performance"] / max(x["price"], 1.0)),
                default=None
            )
            if best_val and not best_val.get("badge"):
                best_val["badge"] = "Best Value"

            # LLM Enhancement for top pick if GEMINI_API_KEY or OPENAI_API_KEY is present
            top_product = scored_products[0]
            query_str = plan.get("original_query", context.get("query", ""))
            llm_text = await self._generate_llm_explanation(top_product, query_str)
            if llm_text:
                top_product["recommendation_explanation"] = f"{llm_text} ({top_product['recommendation_explanation']})"

        if on_progress:
            await on_progress(self.name, "progress", f"Ranked {len(scored_products)} products. Top candidate: {scored_products[0].get('name') if scored_products else 'None'} ({scored_products[0].get('score_overall') if scored_products else 0}%).", None)

        return {
            "ranked_products": scored_products
        }

    async def _generate_llm_explanation(self, product: Dict[str, Any], query: str) -> Optional[str]:
        """Optionally synthesizes grounded natural-language justification via Gemini / OpenAI when configured in .env"""
        if not (settings.GEMINI_API_KEY or settings.OPENAI_API_KEY):
            return None

        prompt = (
            f"You are an expert e-commerce shopping advisor. A user requested: '{query}'. "
            f"We selected this top recommendation: '{product.get('name')}' priced at ₹{product.get('price'):,.0f} "
            f"with specs: {product.get('specifications')}. "
            f"Provide a concise 2-sentence rationale directly explaining why this product satisfies their specific goal. "
            f"Do not hallucinate features not present in specs."
        )

        try:
            if settings.GEMINI_API_KEY:
                async with httpx.AsyncClient(timeout=8.0) as client:
                    resp = await client.post(
                        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}",
                        json={"contents": [{"parts": [{"text": prompt}]}]}
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
                        if parts and "text" in parts[0]:
                            return parts[0]["text"].strip()
            elif settings.OPENAI_API_KEY:
                async with httpx.AsyncClient(timeout=8.0) as client:
                    resp = await client.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                        json={
                            "model": "gpt-4o-mini",
                            "messages": [{"role": "user", "content": prompt}],
                            "max_tokens": 150
                        }
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        return data["choices"][0]["message"]["content"].strip()
        except Exception:
            pass
        return None
