# System Design & Architecture: E-Commerce AI Multi-Agent Shopping Assistant

## Overview
The platform coordinates a cooperative swarm of 10 specialized AI agents to analyze natural-language shopping requests, extract hardware constraints, search authorized vendor catalogs, audit customer reviews, compute price intelligence, and rank recommendations with transparent justifications.

```mermaid
flowchart TD
    User["👤 User Request"] --> UI["💻 React + Vite + Tailwind Frontend"]
    UI --> API["⚡ FastAPI Gateway & Auth Middleware"]
    API --> Orchestrator["🤖 Orchestrator Agent"]
    
    subgraph AgentSwarm["Multi-Agent Cooperative Swarm"]
        Orchestrator --> Planner["1. Shopping Planner Agent"]
        Planner --> SearchAgent["2. Product Search Agent"]
        SearchAgent --> BrowserAgent["Playwright Browser Automation"]
        SearchAgent --> ExtractionAgent["3. Product Extraction Agent"]
        ExtractionAgent --> SafetyAgent["4. Product Safety / Trust Agent"]
        ExtractionAgent --> BudgetAgent["5. Budget Intelligence Agent"]
        SafetyAgent --> ReviewAgent["6. Review Analysis Agent"]
        ReviewAgent --> PriceAgent["7. Price Intelligence Agent"]
        PriceAgent --> CompAgent["8. Product Comparison Agent"]
        CompAgent --> RAGSystem["RAG Knowledge Engine"]
        RAGSystem --> RecAgent["9. Recommendation Agent"]
        RecAgent --> HumanLoop["10. Human-in-the-Loop Checkout Agent"]
    end
    
    HumanLoop --> Approval{"⚠️ User Confirmation Required"}
    Approval -->|Confirmed| CheckoutSession["Redirect to Authorized Merchant"]
    Approval -->|Cancelled| Abort["Abort Transaction"]
    
    AgentSwarm -.->|Live SSE / WS Stream| UI
    AgentSwarm --> DB[("🐘 PostgreSQL / SQLite DB")]
```

## Multi-Factor Recommendation Algorithm
The Recommendation Agent calculates overall match through an empirical weighted formula:

$$\text{Score} = (0.30 \times \text{Match}) + (0.25 \times \text{Price}) + (0.20 \times \text{Perf}) + (0.15 \times \text{Reviews}) + (0.05 \times \text{Trust}) + (0.05 \times \text{Warranty})$$

- **Requirement Match (30%)**: Verifies RAM, SSD, GPU, and processor specs.
- **Price Justification (25%)**: Scores distance below maximum budget ceiling.
- **Hardware Performance (20%)**: CUDA capability, TGP wattage, NPU TOPS, and core counts.
- **Buyer Reviews (15%)**: Normalized rating and aspect sentiment.
- **Trust & Warranty (10%)**: Authentic seller verification and warranty coverage.
