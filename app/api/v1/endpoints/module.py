from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.depedencies.module import get_module_service
from app.services.module import ModuleService
from app.api.v1.schemas.auth import (
    ModuleCreate,
    ModuleUpdate,
    ModuleResponse,
)
from app.api.v1.schemas.response import SuccessResponse
from app.utils.logger import logger
from app.utils.message import Message

msg = Message("Module")

router = APIRouter(
    prefix="/modules",
    tags=["Modules"]
)


@router.post("/", response_model=SuccessResponse)
async def create_module(
    payload: ModuleCreate,
    db: AsyncSession = Depends(get_db),
    service: ModuleService = Depends(get_module_service)
):
    result = await service.create_module(
        db,
        payload.model_dump(),
        created_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.created(), extra={"module_id": str(result.id)})

    return SuccessResponse(
        message=msg.created(),
        data=ModuleResponse.model_validate(result)
    )


@router.get("/", response_model=SuccessResponse)
async def get_modules(
    search: str | None = None,
    sort_by: str | None = None,
    sort_order: str = "asc",
    db: AsyncSession = Depends(get_db),
    service: ModuleService = Depends(get_module_service)
):
    result = await service.get_all_modules(
        db,
        search,
        sort_by,
        sort_order
    )

    logger.info(msg.fetched(), extra={"count": len(result)})

    return SuccessResponse(
        message=msg.fetched(),
        data=[
            ModuleResponse.model_validate(module)
            for module in result
        ]
    )


@router.get("/{module_id}", response_model=SuccessResponse)
async def get_module(
    module_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: ModuleService = Depends(get_module_service)
):
    result = await service.get_module(
        db,
        module_id
    )

    logger.info(
        msg.fetched(),
        extra={"module_id": str(module_id)}
    )

    return SuccessResponse(
        message=msg.fetched(),
        data=ModuleResponse.model_validate(result)
    )


@router.put("/{module_id}", response_model=SuccessResponse)
async def update_module(
    module_id: UUID,
    payload: ModuleUpdate,
    db: AsyncSession = Depends(get_db),
    service: ModuleService = Depends(get_module_service)
):
    result = await service.update_module(
        db,
        module_id,
        payload.model_dump(exclude_unset=True),
        updated_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(
        msg.updated(),
        extra={"module_id": str(module_id)}
    )

    return SuccessResponse(
        message=msg.updated(),
        data=ModuleResponse.model_validate(result)
    )


@router.delete("/{module_id}", response_model=SuccessResponse)
async def delete_module(
    module_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: ModuleService = Depends(get_module_service)
):
    result = await service.delete_module(
        db,
        module_id,
        deleted_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.warning(
        msg.deleted(),
        extra={"module_id": str(module_id)}
    )

    return SuccessResponse(
        message=msg.deleted(),
        data=ModuleResponse.model_validate(result)
    )