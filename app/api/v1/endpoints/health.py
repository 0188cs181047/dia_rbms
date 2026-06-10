from fastapi import APIRouter

from app.api.v1.schemas.response import success_response, error_response
from app.services.health import HealthService

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/cache")
async def cache_health_check():

    result = await HealthService.cache_health()

    if result["status"] == "connected":
        return success_response(
            message=f"{result['cache_type']} is connected successfully",
            data=result
        )

    return error_response(
        message="Cache connection failed",
        error_code="CACHE_CONNECTION_ERROR",
        details=result
    )