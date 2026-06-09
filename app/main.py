from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.app_router import app_route
from app.core.middleware.exception_handler import ExceptionMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

ExceptionMiddleware(app)

app.include_router(app_route)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )