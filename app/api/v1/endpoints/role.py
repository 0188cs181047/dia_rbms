from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.schemas.response import SuccessResponse
from app.api.v1.schemas.auth import (
    RoleCreate,
    RoleUpdate,
    RoleResponse,
)
from app.db.dependencies import get_db
from app.depedencies.role import get_role_service
from app.services.role import RoleService
from app.utils.logger import logger
from app.utils.message import Message

msg = Message("Role")

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post("/", response_model=SuccessResponse)
async def create_role(
    payload: RoleCreate,
    db: AsyncSession = Depends(get_db),
    service: RoleService = Depends(get_role_service)
):
    result = await service.create_role(
        db,
        payload.model_dump(),
        created_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.created(), extra={"role_id": str(result.id)})

    return SuccessResponse(
        message=msg.created(),
        data=RoleResponse.model_validate(result)
    )


@router.get("/", response_model=SuccessResponse)
async def get_roles(
    search: str | None = None,
    sort_by: str | None = None,
    sort_order: str = "asc",
    db: AsyncSession = Depends(get_db),
    service: RoleService = Depends(get_role_service)
):
    result = await service.get_all_roles(
        db,
        search,
        sort_by,
        sort_order
    )

    return SuccessResponse(
        message=msg.fetched(),
        data=[
            RoleResponse.model_validate(role)
            for role in result
        ]
    )


@router.get("/{role_id}", response_model=SuccessResponse)
async def get_role(
    role_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: RoleService = Depends(get_role_service)
):
    result = await service.get_role(
        db,
        role_id
    )

    return SuccessResponse(
        message=msg.fetched(),
        data=RoleResponse.model_validate(result)
    )


@router.put("/{role_id}", response_model=SuccessResponse)
async def update_role(
    role_id: UUID,
    payload: RoleUpdate,
    db: AsyncSession = Depends(get_db),
    service: RoleService = Depends(get_role_service)
):
    result = await service.update_role(
        db,
        role_id,
        payload.model_dump(exclude_unset=True),
        updated_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    return SuccessResponse(
        message=msg.updated(),
        data=RoleResponse.model_validate(result)
    )


@router.delete("/{role_id}", response_model=SuccessResponse)
async def delete_role(
    role_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: RoleService = Depends(get_role_service)
):
    result = await service.delete_role(
        db,
        role_id,
        deleted_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    return SuccessResponse(
        message=msg.deleted(),
        data=RoleResponse.model_validate(result)
    )