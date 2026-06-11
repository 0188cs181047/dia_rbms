from fastapi import APIRouter
from app.api.v1.endpoints.tests import router as test_router
from app.api.v1.endpoints.health import router as helth_router
from app.api.v1.endpoints.country import router as country_router
from app.api.v1.endpoints.state import router as state_router
from app.api.v1.endpoints.city import router as city_router

router = APIRouter()

router.include_router(test_router)
router.include_router(helth_router)
router.include_router(country_router)
router.include_router(state_router)
router.include_router(city_router)