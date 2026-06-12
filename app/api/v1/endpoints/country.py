from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.dependencies import get_db
from app.depedencies.country import get_country_service
from app.api.v1.schemas.masters import CountryCreate, CountryUpdate, CountryResponse
from app.services.country import CountryService
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.logger import logger
from app.api.v1.schemas.response import SuccessResponse
from app.utils.message import Message

msg = Message("Country")

router = APIRouter(prefix="/countries", tags=["Countries"])

@router.post("/", response_model=SuccessResponse)
async def create_country(
    payload: CountryCreate,
    db: AsyncSession = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    result = await service.create_country(
        db,
        payload.model_dump(),
        created_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.created(), extra={"country": result.id})

    return SuccessResponse(
        message=msg.created(),
        data=CountryResponse.model_validate(result)
    )

@router.get("/", response_model=SuccessResponse)
async def get_countries(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None,
    sort_by: str | None = None,
    sort_order: str = "asc",
    db: AsyncSession = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    result = await service.get_all_countries(
        db,
        skip,
        limit,
        search,
        sort_by,
        sort_order
    )

    logger.info(msg.fetched(), extra={"count": len(result)})

    return SuccessResponse(
        message=msg.fetched(),
        data=[CountryResponse.model_validate(res) for res in result]
    )

@router.get("/{country_id}", response_model=SuccessResponse)
async def get_country(
    country_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    result = await service.get_country(db, country_id)

    logger.info(msg.fetched(), extra={"country_id": str(country_id)})

    return SuccessResponse(
        message=msg.fetched(),
        data=CountryResponse.model_validate(result)
    )


@router.put("/{country_id}", response_model=SuccessResponse)
async def update_country(
    country_id: UUID,
    payload: CountryUpdate,
    db: AsyncSession = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    result = await service.update_country(
        db,
        country_id,
        payload.model_dump(exclude_unset=True),
        updated_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.updated(), extra={"country_id": str(country_id)})

    return SuccessResponse(
        message=msg.updated(),
        data=CountryResponse.model_validate(result)
    )

@router.delete("/{country_id}", response_model=SuccessResponse)
async def delete_country(
    country_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    result = await service.delete_country(db, country_id, deleted_by="3fa85f64-5717-4562-b3fc-2c963f66afa6")

    logger.warning(msg.deleted(), extra={"country_id": str(country_id)})

    return SuccessResponse(
        message=msg.deleted(),
        data=CountryResponse.model_validate(result)
    )