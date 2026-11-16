from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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


@app.get("/")
async def root():
    return {
        "message": "Welcome to the E-Commerce AI Multi-Agent Shopping Assistant API",
        "docs_url": "/docs",
        "version": "1.0.0"
    }
