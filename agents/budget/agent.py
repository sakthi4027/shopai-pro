from typing import Dict, Any, Optional, List
from agents.base_agent import AbstractAgent


class BudgetAgent(AbstractAgent):
    """
    Evaluates pricing against user's explicit or memory budget.
    Classifies each candidate as Within Budget, Near Budget, or Over Budget.
    Guarantees products substantially over budget are never recommended without explicit warning.
    """
    def __init__(self):
        super().__init__(
            name="Budget Intelligence Agent",
            description="Enforces strict budget constraints and categorizes items by affordability"
        )

    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        plan = context.get("plan", {})
        budget_max = plan.get("budget_max")
        items = context.get("verified_products", [])

        within_budget = []
        near_budget = []
        over_budget = []
        annotated_items = []

        for p in items:
            price = p.get("price", 0.0)
            p_copy = dict(p)

            if not budget_max:
                p_copy["budget_status"] = "Within Budget"
                p_copy["budget_diff"] = 0.0
                within_budget.append(p_copy)
            else:
                diff = price - budget_max
                p_copy["budget_diff"] = round(diff, 2)
                
                if price <= budget_max:
                    p_copy["budget_status"] = "Within Budget"
                    p_copy["budget_note"] = f"₹{abs(diff):,.0f} under budget"
                    within_budget.append(p_copy)
                elif price <= (budget_max * 1.10):  # Within 10% tolerance
                    p_copy["budget_status"] = "Near Budget"
                    p_copy["budget_note"] = f"₹{diff:,.0f} slightly above budget (+{round((diff/budget_max)*100, 1)}%)"
                    near_budget.append(p_copy)
                else:
                    p_copy["budget_status"] = "Over Budget"
                    p_copy["budget_note"] = f"₹{diff:,.0f} over budget (+{round((diff/budget_max)*100, 1)}%)"
                    over_budget.append(p_copy)

            annotated_items.append(p_copy)

        if on_progress:
            budget_str = f"₹{budget_max:,.0f}" if budget_max else "No limit"
            await on_progress(self.name, "progress", f"Budget {budget_str}: {len(within_budget)} within budget, {len(near_budget)} near budget, {len(over_budget)} over budget.", None)

        return {
            "within_budget": within_budget,
            "near_budget": near_budget,
            "over_budget": over_budget,
            "budget_annotated_products": annotated_items
        }
