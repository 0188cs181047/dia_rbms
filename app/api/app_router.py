from fastapi import APIRouter
from app.api.v1.router import router as v1_router

app_route = APIRouter()

app_route.include_router(v1_router)



