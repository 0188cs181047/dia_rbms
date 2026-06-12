from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.api.app_router import app_route
from app.core.middleware.exception_handler import ExceptionMiddleware

from app.integrations.caching.cache_manager import init_cache, get_cache

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_cache()

    yield

    cache = get_cache()
    await cache.disconnect()


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ExceptionMiddleware(app)

app.include_router(app_route)