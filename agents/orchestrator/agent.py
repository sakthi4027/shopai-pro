import asyncio
import logging
from typing import Dict, Any, Optional, Callable, List
from agents.planner.agent import ShoppingPlannerAgent
from agents.search.agent import ProductSearchAgent
from agents.extraction.agent import ProductExtractionAgent
from agents.trust.agent import ProductTrustAgent
from agents.budget.agent import BudgetAgent
from agents.review.agent import ReviewAnalysisAgent
from agents.price.agent import PriceIntelligenceAgent
from agents.comparison.agent import ProductComparisonAgent
from agents.recommendation.agent import RecommendationAgent
from agents.checkout.agent import HumanInTheLoopCheckoutAgent
from agents.verification.agent import FactVerificationAgent
from agents.conversation.agent import ConversationAgent
from backend.app.rag.engine import rag_engine

logger = logging.getLogger("orchestrator")


class OrchestratorAgent:
    """
    Central Coordinator for the Conversational E-Commerce Deep Search AI Agent.
    Manages multi-agent workflow DAG, supports multi-turn memory and active constraints,
    handles agent timeouts, coordinates fact verification and conversational synthesis,
    emits real-time SSE telemetry events, and guarantees human-in-the-loop safety.
    """
    def __init__(self):
        self.planner = ShoppingPlannerAgent()
        self.searcher = ProductSearchAgent()
        self.extractor = ProductExtractionAgent()
        self.trust_agent = ProductTrustAgent()
        self.budget_agent = BudgetAgent()
        self.review_agent = ReviewAnalysisAgent()
        self.price_agent = PriceIntelligenceAgent()
        self.comparison_agent = ProductComparisonAgent()
        self.recommendation_agent = RecommendationAgent()
        self.verification_agent = FactVerificationAgent()
        self.conversation_agent = ConversationAgent()
        self.checkout_agent = HumanInTheLoopCheckoutAgent()

    async def execute_workflow(
        self,
        query: str,
        user_preferences: Optional[Dict[str, Any]] = None,
        custom_budget_max: Optional[float] = None,
        active_constraints: Optional[Dict[str, Any]] = None,
        search_mode: str = "deep",
        on_event: Optional[Callable[[str, str, str, Optional[Dict[str, Any]]], Any]] = None
    ) -> Dict[str, Any]:
        """
        Executes the end-to-end multi-agent pipeline with error isolation and live telemetry.
        """
        workflow_context: Dict[str, Any] = {
            "query": query,
            "user_preferences": user_preferences or {},
            "custom_budget_max": custom_budget_max,
            "active_constraints": active_constraints or {},
            "search_mode": search_mode
        }

        # Step 1: Shopping Planner / Query Understanding
        if on_event:
            await on_event("Shopping Planner", "progress", f"Analyzing query intent and conversational constraints in {search_mode} mode...", None)
        plan_res = await self.planner.run(workflow_context, on_event)
        workflow_context["plan"] = plan_res.data

        # Step 2: Multi-Source Product Search & Discovery
        if on_event:
            await on_event("Product Search Agent", "progress", "Executing multi-source search across Amazon, Flipkart, Croma, and brand stores...", None)
        search_res = await self.searcher.run(workflow_context, on_event)
        workflow_context["search_results"] = search_res.data
        workflow_context["sources_status"] = search_res.data.get("sources_status", [])

        # Step 3: Product Detail Extraction
        if on_event:
            await on_event("Product Extraction Agent", "progress", "Extracting specifications, multi-seller prices, and direct URLs...", None)
        extract_res = await self.extractor.run(workflow_context, on_event)
        workflow_context["extracted_products"] = extract_res.data.get("extracted_products", [])

        # Step 4: Product Safety & Trust Audit
        if on_event:
            await on_event("Product Safety / Trust Agent", "progress", "Auditing seller repute, warranty claims, and filtering deceptive listings...", None)
        trust_res = await self.trust_agent.run(workflow_context, on_event)
        workflow_context["verified_products"] = trust_res.data.get("verified_products", [])
        workflow_context["flagged_products"] = trust_res.data.get("flagged_products", [])

        # Step 5: Budget Intelligence
        if on_event:
            await on_event("Budget Intelligence Agent", "progress", "Categorizing products into Within Budget, Near Budget, and Over Budget...", None)
        budget_res = await self.budget_agent.run(workflow_context, on_event)
        workflow_context["budget_annotated_products"] = budget_res.data.get("budget_annotated_products", [])

        # Step 6: Review Sentiment & Theme Analysis
        if on_event:
            await on_event("Review Analysis Agent", "progress", "Analyzing authentic customer reviews and extracting aspect themes...", None)
        review_res = await self.review_agent.run(workflow_context, on_event)
        workflow_context["reviews_data"] = review_res.data

        # Step 7: Price Intelligence
        if on_event:
            await on_event("Price Intelligence Agent", "progress", "Comparing cross-merchant seller prices and identifying lowest verified offers...", None)
        price_res = await self.price_agent.run(workflow_context, on_event)
        workflow_context["pricing_data"] = price_res.data

        # Step 8: Product Comparison Matrix
        if on_event:
            await on_event("Product Comparison Agent", "progress", "Building side-by-side specification and seller comparison matrix...", None)
        comp_res = await self.comparison_agent.run(workflow_context, on_event)
        workflow_context["comparison_matrix"] = comp_res.data.get("comparison_matrix", [])
        workflow_context["comparison_highlights"] = comp_res.data.get("highlights", {})

        # Step 9: Grounded RAG Knowledge Verification
        rag_answer = rag_engine.generate_grounded_answer(query)
        workflow_context["rag_insight"] = rag_answer

        # Step 10: Multi-Factor Recommendation & Ranking
        if on_event:
            await on_event("Recommendation Agent", "progress", "Computing multi-factor scores (Match, Price, Performance, Reviews, Warranty)...", None)
        rec_res = await self.recommendation_agent.run(workflow_context, on_event)
        ranked = rec_res.data.get("ranked_products", [])
        workflow_context["ranked_products"] = ranked

        # Step 11: Fact Verification
        if on_event:
            await on_event("Verification Agent", "progress", "Auditing product authenticity, live URLs, and price claims...", None)
        verif_res = await self.verification_agent.run(workflow_context, on_event)
        verified_final = verif_res.data.get("verified_products", ranked)
        workflow_context["verified_products"] = verified_final

        # Step 12: Conversational Synthesis
        if on_event:
            await on_event("Conversation Agent", "progress", "Synthesizing conversational response with embedded cards and follow-ups...", None)
        conv_res = await self.conversation_agent.run(workflow_context, on_event)
        conversational_content = conv_res.data.get("conversational_content", "")
        follow_ups = conv_res.data.get("follow_up_suggestions", [])
        transparency = conv_res.data.get("transparency_statement", "")

        if on_event:
            await on_event("Orchestrator", "completed", f"Research complete! Ready to present {len(verified_final)} verified options.", None)

        return {
            "query": query,
            "plan": workflow_context["plan"],
            "ranked_products": verified_final,
            "flagged_products": workflow_context["flagged_products"],
            "comparison_matrix": workflow_context["comparison_matrix"],
            "comparison_highlights": workflow_context["comparison_highlights"],
            "rag_insight": rag_answer,
            "sources_status": workflow_context["sources_status"],
            "conversational_content": conversational_content,
            "follow_up_suggestions": follow_ups,
            "transparency_statement": transparency,
            "total_products_found": len(verified_final)
        }


orchestrator_agent = OrchestratorAgent()
