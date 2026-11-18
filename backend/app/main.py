import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.app.config.settings import settings
from backend.app.database.session import init_db
from backend.app.database.seed import seed_database
from backend.app.api.v1 import (
    auth,
    users,
    preferences,
    search,
    products,
    compare,
    reviews,
    prices,
    recommendations,
    saved,
    alerts,
    agents,
    checkout,
    audit,
    conversations
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB tables and seed default products on startup
    await init_db()
    await seed_database()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Production-grade AI E-Commerce Multi-Agent Shopping Assistant Platform",
    lifespan=lifespan
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all API v1 routers
prefix = settings.API_V1_PREFIX
app.include_router(auth.router, prefix=prefix)
app.include_router(users.router, prefix=prefix)
app.include_router(preferences.router, prefix=prefix)
app.include_router(search.router, prefix=prefix)
app.include_router(products.router, prefix=prefix)
app.include_router(compare.router, prefix=prefix)
app.include_router(reviews.router, prefix=prefix)
app.include_router(prices.router, prefix=prefix)
app.include_router(recommendations.router, prefix=prefix)
app.include_router(saved.router, prefix=prefix)
app.include_router(alerts.router, prefix=prefix)
app.include_router(agents.router, prefix=prefix)
app.include_router(checkout.router, prefix=prefix)
app.include_router(audit.router, prefix=prefix)
app.include_router(conversations.router, prefix=prefix)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "agents_online": 10,
        "mcp_tools_registered": 10,
        "version": "1.0.0"
    }


# Mount Frontend UI directly on Backend
dist_dir = os.path.abspath("frontend/dist")
if os.path.exists(dist_dir) and os.path.exists(os.path.join(dist_dir, "assets")):
    app.mount("/assets", StaticFiles(directory=os.path.join(dist_dir, "assets")), name="static_assets")

    @app.get("/", include_in_schema=False)
    @app.get("/app", include_in_schema=False)
    @app.get("/app/{full_path:path}", include_in_schema=False)
    async def serve_app(full_path: str = ""):
        file_path = os.path.join(dist_dir, full_path)
        if full_path and os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(dist_dir, "index.html"))

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa_fallback(full_path: str):
        if full_path.startswith("api") or full_path.startswith("docs") or full_path.startswith("openapi.json"):
            return None
        file_path = os.path.join(dist_dir, full_path)
        if full_path and os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(dist_dir, "index.html"))
else:
    @app.get("/")
    async def root():
        return {
            "message": "Welcome to the E-Commerce AI Multi-Agent Shopping Assistant API",
            "docs_url": "/docs",
            "version": "1.0.0"
        }

