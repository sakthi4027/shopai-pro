import re
from typing import Dict, Any, Optional, List
from agents.base_agent import AbstractAgent


class ShoppingPlannerAgent(AbstractAgent):
    """
    Parses natural language shopping requests into structured requirements,
    supporting ANY e-commerce shopping domain (phones, laptops, SSDs, shoes, appliances, audio, etc.).
    Maintains multi-turn conversational memory, merges active constraints across follow-up queries,
    and classifies user intents (initial search, constraint refinement, pagination, price comparison).
    """
    def __init__(self):
        super().__init__(
            name="Shopping Planner",
            description="Extracts structured constraints, category hierarchies, and multi-turn intents from freeform user requests"
        )

    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        query = context.get("query", "").strip()
        user_memory = context.get("user_preferences", {})
        custom_budget = context.get("custom_budget_max")
        previous_constraints = context.get("active_constraints", {})

        # 0. Intent Classification
        is_reset = bool(re.search(r'\b(new search|reset|start over|clear search|new conversation)\b', query, re.IGNORECASE))
        is_pagination = bool(re.search(r'\b(show next|load more|more results|next page|page 2|products [0-9]+-[0-9]+)\b', query, re.IGNORECASE))
        is_comparison = bool(re.search(r'\b(compare|versus|vs\.?|difference between)\b', query, re.IGNORECASE))
        is_cheapest_seller = bool(re.search(r'\b(cheapest|lowest price|best price|where is this cheapest|where to buy)\b', query, re.IGNORECASE))
        is_best_reviews = bool(re.search(r'\b(best reviews|highest rated|top rated|best ratings)\b', query, re.IGNORECASE))
        
        # Check if this is a follow-up refinement (e.g. "Only Lenovo", "under 50k", "need 32GB RAM")
        is_follow_up = bool(previous_constraints) and not is_reset and len(query.split()) <= 8

        # 1. Budget extraction
        extracted_budget = None
        if custom_budget:
            extracted_budget = float(custom_budget)
        else:
            # Look for lakh
            lakh_match = re.search(r'(?:under|below|less than|within|budget of)?\s*(?:₹|rs\.?|inr)?\s*([0-9\.]+)\s*(?:lakh|lac)', query, re.IGNORECASE)
            if lakh_match:
                extracted_budget = float(lakh_match.group(1)) * 100000.0
            else:
                # Look for k (e.g. 80k, 5k)
                k_match = re.search(r'(?:under|below|less than|within|budget of)?\s*(?:₹|rs\.?|inr)?\s*([0-9\.]+)\s*k\b', query, re.IGNORECASE)
                if k_match:
                    extracted_budget = float(k_match.group(1)) * 1000.0
                else:
                    # Look for raw number
                    num_match = re.search(r'(?:under|below|less than|within|budget(?:\s*of)?)\s*(?:₹|rs\.?|inr)?\s*([0-9,]{3,7})', query, re.IGNORECASE)
                    if num_match:
                        raw_num = num_match.group(1).replace(",", "")
                        try:
                            extracted_budget = float(raw_num)
                        except ValueError:
                            pass
        
        # Inherit previous budget if follow-up and none specified
        if not extracted_budget and is_follow_up and previous_constraints.get("budget_max"):
            extracted_budget = previous_constraints["budget_max"]
        elif not extracted_budget and user_memory.get("budget_max"):
            extracted_budget = float(user_memory["budget_max"])

        # 2. Category Detection across ALL consumer products
        category = "general"
        if re.search(r'\b(laptop|notebook|macbook|thinkpad|gaming pc)\b', query, re.IGNORECASE):
            category = "laptop"
        elif re.search(r'\b(phone|smartphone|iphone|android|mobile|galaxy s|pixel)\b', query, re.IGNORECASE):
            category = "smartphone"
        elif re.search(r'\b(ssd|hard drive|nvme|hdd|storage drive|thumb drive)\b', query, re.IGNORECASE):
            category = "storage"
        elif re.search(r'\b(shoe|shoes|sneaker|sneakers|running shoe|footwear|boots)\b', query, re.IGNORECASE):
            category = "footwear"
        elif re.search(r'\b(washing machine|refrigerator|fridge|microwave|air conditioner|ac|vacuum)\b', query, re.IGNORECASE):
            category = "appliance"
        elif re.search(r'\b(headphone|headphones|earphone|earphones|airpod|airpods|earbud|earbuds|speaker)\b', query, re.IGNORECASE):
            category = "audio"
        elif re.search(r'\b(monitor|display|screen|tv|television)\b', query, re.IGNORECASE):
            category = "monitor"
        elif re.search(r'\b(watch|smartwatch|fitness tracker|band)\b', query, re.IGNORECASE):
            category = "wearable"
        elif re.search(r'\b(rtx|gpu|graphics card|cpu|processor|motherboard|ram)\b', query, re.IGNORECASE):
            category = "component"
        elif is_follow_up and previous_constraints.get("category"):
            category = previous_constraints["category"]

        # 3. Features extraction
        required_features = list(previous_constraints.get("required_features", [])) if is_follow_up else []
        preferred_features = list(previous_constraints.get("preferred_features", [])) if is_follow_up else []
        optional_features = list(previous_constraints.get("optional_features", [])) if is_follow_up else []
        excluded_features = list(previous_constraints.get("excluded_features", [])) if is_follow_up else []

        # RAM requirement
        ram_match = re.search(r'([0-9]+)\s*(?:gb|gig)\s*(?:ram|memory)?', query, re.IGNORECASE)
        if ram_match:
            ram_val = int(ram_match.group(1))
            rf_str = f"{ram_val}GB RAM"
            if rf_str not in required_features:
                required_features.append(rf_str)
        elif not required_features and user_memory.get("preferred_ram"):
            required_features.append(f"{user_memory['preferred_ram']} RAM")

        # Storage requirement
        storage_match = re.search(r'([0-9]+)\s*(?:tb|terabyte)\s*(?:ssd|storage|nvme|hdd)?', query, re.IGNORECASE)
        if not storage_match:
            storage_match = re.search(r'([0-9]+)\s*(?:gb|gig)\s*(?:ssd|storage|nvme|hdd)\b', query, re.IGNORECASE)
        
        if storage_match:
            storage_str = storage_match.group(0).upper().strip()
            if storage_str not in required_features:
                required_features.append(storage_str)
        elif not any("STORAGE" in f or "SSD" in f or "TB" in f for f in required_features) and user_memory.get("preferred_storage"):
            required_features.append(f"{user_memory['preferred_storage']} Storage")

        # GPU / AI Development
        if re.search(r'\b(ai|deep learning|machine learning|ml|data science|pytorch|tensorflow|cuda)\b', query, re.IGNORECASE):
            if "CUDA / Dedicated GPU" not in required_features:
                required_features.append("CUDA / Dedicated GPU")
            if "AI Acceleration / High NPU/GPU TOPS" not in preferred_features:
                preferred_features.append("AI Acceleration / High NPU/GPU TOPS")

        if re.search(r'\b(rtx|gpu|nvidia|graphics)\b', query, re.IGNORECASE):
            if "NVIDIA RTX Dedicated GPU" not in required_features:
                required_features.append("NVIDIA RTX Dedicated GPU")

        # Specific GPU numbers e.g. RTX 4060, RTX 5070
        rtx_match = re.search(r'rtx\s*([0-9]{4})', query, re.IGNORECASE)
        if rtx_match:
            gpu_num = rtx_match.group(1)
            required_features.append(f"RTX {gpu_num} GPU")

        # Battery
        if re.search(r'\b(battery|long battery|good battery life|all-day battery)\b', query, re.IGNORECASE):
            if "High Battery Life (>= 7 hours)" not in preferred_features:
                preferred_features.append("High Battery Life (>= 7 hours)")

        # Brand preferences: explicit query brands always take precedence over inherited memory
        brands_to_check = [
            "ASUS", "Lenovo", "Dell", "HP", "Apple", "Acer", "MSI", "Samsung", "Sony", 
            "OnePlus", "Xiaomi", "Realme", "Nike", "Adidas", "Puma", "Crucial", "Kingston",
            "LG", "Whirlpool", "Bosch", "IFB", "Haier"
        ]
        explicit_brands = []
        for b in brands_to_check:
            if re.search(rf'\b{b}\b', query, re.IGNORECASE):
                if b not in explicit_brands:
                    explicit_brands.append(b)

        if explicit_brands:
            preferred_brands = explicit_brands
        elif is_follow_up and previous_constraints.get("preferred_brands"):
            preferred_brands = list(previous_constraints["preferred_brands"])
        elif user_memory.get("preferred_brands"):
            preferred_brands = list(user_memory["preferred_brands"])
        else:
            preferred_brands = []

        # Exclusions (e.g. refurbished, used, gaming)
        if re.search(r'\b(exclude gaming|no gaming)\b', query, re.IGNORECASE):
            excluded_features.append("Gaming Laptops")

        if user_memory.get("avoid_refurbished", True) or re.search(r'\b(avoid refurbished|no refurbished|new only)\b', query, re.IGNORECASE):
            if "Refurbished / Open Box" not in excluded_features:
                excluded_features.append("Refurbished / Open Box")

        if user_memory.get("excluded_keywords"):
            for ek in user_memory["excluded_keywords"]:
                if ek not in excluded_features:
                    excluded_features.append(ek)

        # Construct context-aware search query
        clean_q = re.sub(r'\b(only|just|show me|find me)\b', '', query, flags=re.IGNORECASE).strip()
        if is_follow_up:
            search_query = f"{' '.join(preferred_brands)} {category} {' '.join(required_features)} {clean_q}".strip()
        else:
            search_query = query

        output_plan = {
            "category": category,
            "budget_max": extracted_budget,
            "required_features": required_features,
            "preferred_features": preferred_features,
            "optional_features": optional_features,
            "excluded_features": excluded_features,
            "preferred_brands": preferred_brands,
            "original_query": query,
            "search_query": search_query,
            "intent": {
                "is_follow_up": is_follow_up,
                "is_pagination": is_pagination,
                "is_comparison": is_comparison,
                "is_cheapest_seller": is_cheapest_seller,
                "is_best_reviews": is_best_reviews,
                "is_reset": is_reset,
                "search_mode": context.get("search_mode", "deep")
            }
        }

        if on_progress:
            await on_progress(
                self.name, 
                "progress", 
                f"Understood request for '{category}'. Budget: {'₹' + f'{extracted_budget:,.0f}' if extracted_budget else 'Flexible'}. Required: {', '.join(required_features) if required_features else 'Standard specs'}.", 
                output_plan
            )

        return output_plan
