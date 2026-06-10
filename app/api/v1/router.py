from fastapi import APIRouter
from app.api.v1.endpoints.tests import router as test_router
from app.api.v1.endpoints.health import router as helth_router

router = APIRouter()

router.include_router(test_router)
router.include_router(helth_router)