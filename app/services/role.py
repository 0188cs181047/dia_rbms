from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import asc, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.role import RoleRepository


class RoleService:
    def __init__(self, repo: RoleRepository):
        self.repo = repo

    async def create_role(
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

    async def get_role(
        self,
        db: AsyncSession,
        role_id: UUID
    ):
        role = await self.repo.get(db, role_id)

        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found"
            )

        return role

    async def get_all_roles(
        self,
        db: AsyncSession,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str = "asc"
    ):
        return await self.repo.get_multi(
            db=db,
            search=search,
            search_fields=["role_name", "description"],
            order_by=(
                asc(sort_by)
                if sort_order == "asc" and sort_by
                else desc(sort_by)
                if sort_by
                else None
            )
        )

    async def update_role(
        self,
        db: AsyncSession,
        role_id: UUID,
        data: dict,
        updated_by: UUID
    ):
        role = await self.repo.get(db, role_id)

        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found"
            )

        return await self.repo.update(
            db,
            role_id,
            data,
            user_id=updated_by
        )

    async def delete_role(
        self,
        db: AsyncSession,
        role_id: UUID,
        deleted_by: UUID
    ):
        role = await self.repo.get(db, role_id)

        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found"
            )

        return await self.repo.delete(
            db,
            role_id,
            user_id=deleted_by
        )