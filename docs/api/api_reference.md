# REST API Reference: E-Commerce AI Multi-Agent Platform

Base URL: `/api/v1`

## Authentication & Users
- `POST /api/v1/auth/register`: Create user account and isolated workspace.
- `POST /api/v1/auth/login`: Authenticate and receive JWT bearer token.
- `GET /api/v1/auth/me`: Get current authenticated user profile.
- `GET /api/v1/users/profile`: User profile details.

## Shopping Memory & Preferences
- `GET /api/v1/preferences`: Retrieve user's saved shopping memory.
- `PUT /api/v1/preferences`: Update preferred brands, budget, RAM, storage, and exclusions.
- `DELETE /api/v1/preferences`: Reset memory to defaults.

## AI Search & Swarm Orchestration
- `POST /api/v1/search/query`: Submit natural-language request and trigger multi-agent pipeline.
- `GET /api/v1/search/history`: Retrieve past isolated search sessions.
- `GET /api/v1/search/sessions/{id}`: Detailed session metrics.

## Products & Comparison
- `GET /api/v1/products`: Filterable product catalog.
- `GET /api/v1/products/{id}`: Full product specifications, seller pricing, and price history.
- `POST /api/v1/compare`: Generate side-by-side spec delta matrix for selected product IDs.

## Review & Price Intelligence
- `GET /api/v1/reviews/{product_id}`: Customer reviews.
- `GET /api/v1/reviews/{product_id}/analysis`: Aspect sentiment breakdown, warnings, and common complaints.
- `GET /api/v1/prices/{product_id}/sellers`: Cross-merchant pricing comparison.
- `GET /api/v1/prices/{product_id}/history`: Timestamped price trend snapshots.

## Human-in-the-Loop Checkout
- `POST /api/v1/checkout/review`: Generates pre-checkout itemized manifest.
- `POST /api/v1/checkout/confirm`: Explicit user confirmation gate (`[Confirm]` / `[Cancel]`).

## Real-Time Telemetry
- `GET /api/v1/agents/stream/{session_id}`: Server-Sent Events (SSE) progress feed.
- `WS /api/v1/agents/ws/{session_id}`: Bidirectional WebSocket stream.
- `GET /api/v1/agents/tasks/{session_id}`: Agent metrics, confidence, and latency.
