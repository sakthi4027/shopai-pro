# ShopAI: Multi-Agent Shopping Assistant

A production-grade, enterprise-ready **AI E-Commerce Multi-Agent Shopping Assistant** platform.

The system understands natural-language shopping requests, coordinates a team of 10 specialized autonomous agents, verifies product specifications, analyzes customer reviews across multiple aspects, tracks price trends, and provides transparent recommendations with strict **Human-in-the-Loop checkout safety**.

---

## 🌟 Key Capabilities

- **10 Autonomous Cooperative Agents**: Orchestrator, Shopping Planner, Product Search, Extraction, Trust / Safety, Budget, Review Analysis, Price Intelligence, Comparison, and Recommendation Agents.
- **Strict Human-in-the-Loop Gating**: Zero autonomous purchasing. Explicit itemized confirmation (`[Confirm]` / `[Cancel]`) required before purchase assistance. Never stores payment cards.
- **RAG Knowledge Retrieval**: Grounded documentation engine with vector embeddings, cosine similarity, and traceable source citations.
- **Model Context Protocol (MCP)**: 10 MCP-compliant tools with Pydantic v2 schemas, permission checks, timeouts, and structured logging.
- **Real-Time Telemetry**: Dual Server-Sent Events (SSE) and WebSocket feeds providing live agent workflow updates.
- **Playwright Browser Agent**: Safe headless web automation with anti-bot detection and safe "Human action required" pauses.
- **Modern Light-Theme UI**: Built with React 19, Vite, TypeScript, Tailwind CSS, Lucide icons, and Recharts. Includes 15 dedicated pages.
- **Enterprise Security**: JWT auth, RBAC, user isolation, and audit logging.

---

## 🏗️ Multi-Agent Architecture

```text
User Request
     ↓
Shopping Planner Agent (Extracts requirements & shopping memory)
     ↓
Product Search Agent (Live multi-source search & deduplication)
     ↓
Product Extraction Agent (Normalizes RAM, SSD, CPU, GPU, warranty)
     ↓
Product Safety / Trust Agent (Flags unverified claims & suspicious prices)
     ↓
Budget Intelligence Agent (Classifies Within, Near, or Over Budget)
     ↓
Review Analysis Agent (Aspect sentiment analysis & buyer warnings)
     ↓
Price Intelligence Agent (Audits price drops & cross-seller variances)
     ↓
Product Comparison Agent (Builds side-by-side matrices & evaluates winners)
     ↓
Recommendation Agent (Calculates multi-factor score & rationale)
     ↓
Human-in-the-Loop Checkout Gate (Requires explicit approval)
```

---

## 🚀 Quick Start

### 1. Backend Setup
```bash
# Clone the repository
cd "e:\E-Commerce AI Multi-Agent"

# Install backend dependencies
pip install -r requirements.txt

# Run database setup and seed initial catalog
python -m backend.app.database.seed

# Start the FastAPI backend server
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```

Backend API will be accessible at `http://localhost:8000` (Swagger docs at `http://localhost:8000/docs`).

### 2. Frontend Setup
```bash
cd frontend

# Install frontend dependencies
npm install

# Start the Vite development server
npm run dev
```

Frontend UI will be accessible at `http://localhost:5173`.

---

## 🧪 Running Automated Tests

Run the comprehensive pytest suite covering unit, integration, agent, security, and RAG evaluation tests:

```bash
python -m pytest tests -v
```

All 13 test suites validate:
- User isolation & JWT authentication
- 10-Agent swarm coordination
- 10 MCP tools and schema validations
- Human-in-the-loop checkout security and audit trails
- RAG grounding and zero-hallucination prevention
- Playwright browser agent safe pause verification

---

## 📄 License
MIT License. Built for production multi-agent e-commerce shopping assistance.
