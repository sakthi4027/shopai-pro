# Agent Specifications: 10 Cooperative Swarm Agents

1. **Orchestrator Agent**: Manages the Directed Acyclic Graph (DAG) of the shopping workflow, enforces timeouts, orchestrates real-time SSE/WebSocket streams, and handles fallback.
2. **Shopping Planner Agent**: Deconstructs freeform natural language into `{category, budget_max, required_features, preferred_features, optional_features, excluded_features}` and applies user shopping memory.
3. **Product Search Agent**: Searches authorized product feeds, canonicalizes URLs, and detects duplicate listings without data fabrication.
4. **Product Extraction Agent**: Normalizes specifications into standard data types (GBs, Watts, GHz, screen diagonal, warranty months).
5. **Product Safety / Trust Agent**: Flags suspiciously low pricing, unverified sellers, missing warranties, and misleading claims.
6. **Budget Intelligence Agent**: Categorizes products into Within Budget, Near Budget, and Over Budget.
7. **Review Analysis Agent**: Classifies aspect sentiment across battery, thermals, performance, display, and build quality.
8. **Price Intelligence Agent**: Audits observed price drops, validates discount percentages, and compares seller offers.
9. **Product Comparison Agent**: Builds side-by-side spec comparison matrices and flags category winners.
10. **Recommendation Agent**: Computes weighted scores and generates transparent, grounded rationales.
11. **Human-In-The-Loop Checkout Agent**: Enforces the zero-autonomous-purchase guarantee and requires explicit user approval.
