from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import asc, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.role_permission import RolePermissionRepository


class RolePermissionService:
    def __init__(self, repo: RolePermissionRepository):
        self.repo = repo

    async def create_role_permission(
        self,
        db: AsyncSession,
        data: dict,
        created_by: UUID
    ):
        return await self.repo.create(
            db,
            data,
            user_id=created_by
        )

    async def get_role_permission(
        self,
        db: AsyncSession,
        rp_id: UUID
    ):
        rp = await self.repo.get(db, rp_id)

        if not rp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="RolePermission not found"
            )

        return rp

    async def get_all_role_permissions(
        self,
        db: AsyncSession,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str = "asc"
    ):
        return await self.repo.get_multi(
            db=db,
            search=search,
            search_fields=["role_id", "permission_id"],
            order_by=(
                asc(sort_by)
                if sort_order == "asc" and sort_by
                else desc(sort_by)
                if sort_by
                else None
            )
        )

    async def update_role_permission(
        self,
        db: AsyncSession,
        rp_id: UUID,
        data: dict,
        updated_by: UUID
    ):
        rp = await self.repo.get(db, rp_id)

        if not rp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="RolePermission not found"
            )

        return await self.repo.update(
            db,
            rp_id,
            data,
            user_id=updated_by
        )

    async def delete_role_permission(
        self,
        db: AsyncSession,
        rp_id: UUID,
        deleted_by: UUID
    ):
        rp = await self.repo.get(db, rp_id)

        if not rp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="RolePermission not found"
            )

        return await self.repo.delete(
            db,
            rp_id,
            user_id=deleted_by
        )