from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.schemas.response import SuccessResponse
from app.api.v1.schemas.auth import (
    PermissionCreate,
    PermissionUpdate,
    PermissionResponse,
)
from app.db.dependencies import get_db
from app.depedencies.permission import get_permission_service
from app.services.permission import PermissionService
from app.utils.logger import logger
from app.utils.message import Message

msg = Message("Permission")

router = APIRouter(
    prefix="/permissions",
    tags=["Permissions"]
)


@router.post("/", response_model=SuccessResponse)
async def create_permission(
    payload: PermissionCreate,
    db: AsyncSession = Depends(get_db),
    service: PermissionService = Depends(get_permission_service)
):
    result = await service.create_permission(
        db,
        payload.model_dump(),
        created_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.created(), extra={"permission_id": str(result.id)})

    return SuccessResponse(
        message=msg.created(),
        data=PermissionResponse.model_validate(result)
    )


@router.get("/", response_model=SuccessResponse)
async def get_permissions(
    search: str | None = None,
    sort_by: str | None = None,
    sort_order: str = "asc",
    db: AsyncSession = Depends(get_db),
    service: PermissionService = Depends(get_permission_service)
):
    result = await service.get_all_permissions(
        db,
        search,
        sort_by,
        sort_order
    )

    return SuccessResponse(
        message=msg.fetched(),
        data=[
            PermissionResponse.model_validate(p)
            for p in result
        ]
    )


@router.get("/{permission_id}", response_model=SuccessResponse)
async def get_permission(
    permission_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: PermissionService = Depends(get_permission_service)
):
    result = await service.get_permission(db, permission_id)

    return SuccessResponse(
        message=msg.fetched(),
        data=PermissionResponse.model_validate(result)
    )


@router.put("/{permission_id}", response_model=SuccessResponse)
async def update_permission(
    permission_id: UUID,
    payload: PermissionUpdate,
    db: AsyncSession = Depends(get_db),
    service: PermissionService = Depends(get_permission_service)
):
    result = await service.update_permission(
        db,
        permission_id,
        payload.model_dump(exclude_unset=True),
        updated_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    return SuccessResponse(
        message=msg.updated(),
        data=PermissionResponse.model_validate(result)
    )


@router.delete("/{permission_id}", response_model=SuccessResponse)
async def delete_permission(
    permission_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: PermissionService = Depends(get_permission_service)
):
    result = await service.delete_permission(
        db,
        permission_id,
        deleted_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    return SuccessResponse(
        message=msg.deleted(),
        data=PermissionResponse.model_validate(result)
    )