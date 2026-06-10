from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.schemas.response import success_response, error_response
from app.services.health import HealthService
from app.db.dependencies import get_db

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

@router.get("/db")
async def check_db_connection(db: AsyncSession = Depends(get_db)):

    result = await HealthService.check_health(db)

    if result["status"] == "connected":
        return success_response(
            message="Database is connected successfully",
            data=result
        )

    return error_response(
        message="Database connection failed",
        error_code="DB_CONNECTION_ERROR",
        details=result
    )
