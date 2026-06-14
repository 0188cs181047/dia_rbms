from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import asc, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.module import ModuleRepository


class ModuleService:
    def __init__(self, repo: ModuleRepository):
        self.repo = repo

    async def create_module(
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

    async def get_module(
        self,
        db: AsyncSession,
        module_id: UUID
    ):
        module = await self.repo.get(db, module_id)

        if not module:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Module not found"
            )

        return module

    async def get_all_modules(
        self,
        db: AsyncSession,
        search=None,
        sort_by=None,
        sort_order="asc"
    ):
        return await self.repo.get_multi(
            db=db,
            search=search,
            search_fields=["name", "code"],
            order_by=(
                asc(sort_by)
                if sort_order == "asc" and sort_by
                else desc(sort_by)
                if sort_by
                else None
            )
        )

    async def update_module(
        self,
        db: AsyncSession,
        module_id: UUID,
        data: dict,
        updated_by: UUID
    ):
        module = await self.repo.get(db, module_id)

        if not module:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Module not found"
            )

        return await self.repo.update(
            db,
            module_id,
            data,
            user_id=updated_by
        )

    async def delete_module(
        self,
        db: AsyncSession,
        module_id: UUID,
        deleted_by: UUID
    ):
        module = await self.repo.get(db, module_id)

        if not module:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Module not found"
            )

        return await self.repo.delete(
            db,
            module_id,
            user_id=deleted_by
        )