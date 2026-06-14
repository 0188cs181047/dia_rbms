from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.depedencies.role_permission import get_role_permission_service
from app.services.role_permission import RolePermissionService
from app.api.v1.schemas.auth import (
    RolePermissionCreate,
    RolePermissionUpdate,
    RolePermissionResponse,
)
from app.api.v1.schemas.response import SuccessResponse
from app.utils.logger import logger
from app.utils.message import Message

msg = Message("RolePermission")

router = APIRouter(
    prefix="/role-permissions",
    tags=["Role Permissions"]
)


@router.post("/", response_model=SuccessResponse)
async def create_role_permission(
    payload: RolePermissionCreate,
    db: AsyncSession = Depends(get_db),
    service: RolePermissionService = Depends(get_role_permission_service)
):
    result = await service.create_role_permission(
        db,
        payload.model_dump(),
        created_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    logger.info(msg.created(), extra={"role_permission_id": str(result.id)})

    return SuccessResponse(
        message=msg.created(),
        data=RolePermissionResponse.model_validate(result)
    )


@router.get("/", response_model=SuccessResponse)
async def get_role_permissions(
    search: str | None = None,
    sort_by: str | None = None,
    sort_order: str = "asc",
    db: AsyncSession = Depends(get_db),
    service: RolePermissionService = Depends(get_role_permission_service)
):
    result = await service.get_all_role_permissions(
        db,
        search,
        sort_by,
        sort_order
    )

    return SuccessResponse(
        message=msg.fetched(),
        data=[
            RolePermissionResponse.model_validate(rp)
            for rp in result
        ]
    )


@router.get("/{rp_id}", response_model=SuccessResponse)
async def get_role_permission(
    rp_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: RolePermissionService = Depends(get_role_permission_service)
):
    result = await service.get_role_permission(db, rp_id)

    return SuccessResponse(
        message=msg.fetched(),
        data=RolePermissionResponse.model_validate(result)
    )


@router.put("/{rp_id}", response_model=SuccessResponse)
async def update_role_permission(
    rp_id: UUID,
    payload: RolePermissionUpdate,
    db: AsyncSession = Depends(get_db),
    service: RolePermissionService = Depends(get_role_permission_service)
):
    result = await service.update_role_permission(
        db,
        rp_id,
        payload.model_dump(exclude_unset=True),
        updated_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    return SuccessResponse(
        message=msg.updated(),
        data=RolePermissionResponse.model_validate(result)
    )


@router.delete("/{rp_id}", response_model=SuccessResponse)
async def delete_role_permission(
    rp_id: UUID,
    db: AsyncSession = Depends(get_db),
    service: RolePermissionService = Depends(get_role_permission_service)
):
    result = await service.delete_role_permission(
        db,
        rp_id,
        deleted_by="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    return SuccessResponse(
        message=msg.deleted(),
        data=RolePermissionResponse.model_validate(result)
    )