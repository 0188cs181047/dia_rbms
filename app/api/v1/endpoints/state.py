from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.db.dependencies import get_db
from app.depedencies.state import get_state_service
from app.api.v1.schemas.masters import StateCreate, StateUpdate, StateResponse
from app.services.state import StateService
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.logger import logger
from app.api.v1.schemas.response import SuccessResponse
from app.utils.message import Message

msg = Message("State")

router = APIRouter(prefix="/states", tags=["States"])

@router.post("/", response_model=SuccessResponse)
async def create_state(
    payload: StateCreate,
    db: AsyncSession = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    result = await service.create_state(
        db,
        payload.model_dump(),
        created_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.created(), extra={"state": result.id})

    return SuccessResponse(
        message=msg.created(),
        data=StateResponse.model_validate(result)
    )

@router.get("/", response_model=SuccessResponse)
async def get_states(
    search: str | None = None,
    sort_by: str | None = None,
    sort_order: str = "asc",
    db: AsyncSession = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    result = await service.get_all_states(
        db,
        search,
        sort_by,
        sort_order
    )
    logger.info(msg.fetched(), extra={"count": len(result)})

    return SuccessResponse(
        message=msg.fetched(),
        data=[StateResponse.model_validate(res) for res in result]
    )

@router.get("/country/{country_id}")
async def get_states_by_country(
    country_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: StateService = Depends(get_state_service)
):
    res = await service.get_states_by_country(db, country_id)
    logger.info(msg.fetched(), extra={"country_id": str(country_id)})

    return SuccessResponse(
        message=msg.fetched(),
        data=[StateResponse.model_validate(state) for state in res]
    )


@router.get("/{state_id}", response_model=SuccessResponse)
async def get_state(state_id: UUID,
    db: AsyncSession = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    res = await service.get_state(db, state_id)

    logger.info(msg.fetched(), extra={"state_id": str(state_id)})

    return SuccessResponse(
        message=msg.fetched(),
        data=StateResponse.model_validate(res)
    )


@router.put("/{state_id}", response_model=SuccessResponse)
async def update_state(
    state_id: UUID,
    payload: StateUpdate,
    db: AsyncSession = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    result = await service.update_state(
        db,
        state_id,
        payload.model_dump(exclude_unset=True),
        updated_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.updated(), extra={"state_id": str(state_id)})

    return SuccessResponse(
        message=msg.updated(),
        data=StateResponse.model_validate(result)
    )


@router.delete("/{state_id}", response_model=SuccessResponse)
async def delete_state(state_id: UUID,
    db: AsyncSession = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    result = await service.delete_state(db, state_id, deleted_by="3fa85f64-5717-4562-b3fc-2c963f66afa6")

    logger.warning(msg.deleted(), extra={"state_id": str(state_id)})

    return SuccessResponse(
        message=msg.deleted(),
        data=StateResponse.model_validate(result)
    )