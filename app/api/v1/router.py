from fastapi import APIRouter
from app.api.v1.endpoints.tests import router as test_router

router = APIRouter()

router.include_router(test_router)