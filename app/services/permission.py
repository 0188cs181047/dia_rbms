from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import asc, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.permission import PermissionRepository


class PermissionService:
    def __init__(self, repo: PermissionRepository):
        self.repo = repo

    async def create_permission(
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

    async def get_permission(
        self,
        db: AsyncSession,
        permission_id: UUID
    ):
        permission = await self.repo.get(db, permission_id)

        if not permission:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Permission not found"
            )

        return permission

    async def get_all_permissions(
        self,
        db: AsyncSession,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str = "asc"
    ):
        return await self.repo.get_multi(
            db=db,
            search=search,
            search_fields=["action"],
            order_by=(
                asc(sort_by)
                if sort_order == "asc" and sort_by
                else desc(sort_by)
                if sort_by
                else None
            )
        )

    async def update_permission(
        self,
        db: AsyncSession,
        permission_id: UUID,
        data: dict,
        updated_by: UUID
    ):
        permission = await self.repo.get(db, permission_id)

        if not permission:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Permission not found"
            )

        return await self.repo.update(
            db,
            permission_id,
            data,
            user_id=updated_by
        )

    async def delete_permission(
        self,
        db: AsyncSession,
        permission_id: UUID,
        deleted_by: UUID
    ):
        permission = await self.repo.get(db, permission_id)

        if not permission:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Permission not found"
            )

        return await self.repo.delete(
            db,
            permission_id,
            user_id=deleted_by
        )