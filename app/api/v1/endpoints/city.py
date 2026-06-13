from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.depedencies.city import get_city_service
from app.api.v1.schemas.masters import (
    CityCreate,
    CityResponse,
    CityUpdate
)
from app.api.v1.schemas.response import SuccessResponse
from app.services.city import CityService
from app.utils.logger import logger
from app.utils.message import Message

msg = Message("City")

router = APIRouter(prefix="/cities", tags=["Cities"])


@router.post("/", response_model=SuccessResponse)
async def create_city(
    payload: CityCreate,
    db: AsyncSession = Depends(get_db),
    service: CityService = Depends(get_city_service)
):
    result = await service.create_city(
        db,
        payload.model_dump(),
        created_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.created(), extra={"city_id": str(result.id)})

    return SuccessResponse(
        message=msg.created(),
        data=CityResponse.model_validate(result)
    )


@router.get("/", response_model=SuccessResponse)
async def get_cities(
    search: str | None = None,
    sort_by: str | None = None,
    sort_order: str = "asc",
    db: AsyncSession = Depends(get_db),
    service: CityService = Depends(get_city_service)
):
    result = await service.get_all_cities(
        db,
        search,
        sort_by,
        sort_order
    )

    logger.info(msg.fetched(), extra={"count": len(result)})

    return SuccessResponse(
        message=msg.fetched(),
        data=[CityResponse.model_validate(city) for city in result]
    )


@router.get("/state/{state_id}", response_model=SuccessResponse)
async def get_cities_by_state(
    state_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: CityService = Depends(get_city_service)
):
    result = await service.get_cities_by_state(db, state_id)

    logger.info(msg.fetched(), extra={"state_id": str(state_id)})

    return SuccessResponse(
        message=msg.fetched(),
        data=[CityResponse.model_validate(city) for city in result]
    )


@router.get("/{city_id}", response_model=SuccessResponse)
async def get_city(
    city_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: CityService = Depends(get_city_service)
):
    result = await service.get_city(db, city_id)

    logger.info(msg.fetched(), extra={"city_id": str(city_id)})

    return SuccessResponse(
        message=msg.fetched(),
        data=CityResponse.model_validate(result)
    )


@router.put("/{city_id}", response_model=SuccessResponse)
async def update_city(
    city_id: UUID,
    payload: CityUpdate,
    db: AsyncSession = Depends(get_db),
    service: CityService = Depends(get_city_service)
):
    result = await service.update_city(
        db,
        city_id,
        payload.model_dump(exclude_unset=True),
        updated_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.updated(), extra={"city_id": str(city_id)})

    return SuccessResponse(
        message=msg.updated(),
        data=CityResponse.model_validate(result)
    )


@router.delete("/{city_id}", response_model=SuccessResponse)
async def delete_city(
    city_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: CityService = Depends(get_city_service)
):
    result = await service.delete_city(
        db,
        city_id,
        deleted_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.warning(msg.deleted(), extra={"city_id": str(city_id)})

    return SuccessResponse(
        message=msg.deleted(),
        data=CityResponse.model_validate(result)
    )