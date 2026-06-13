from uuid import UUID

from sqlalchemy import asc, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.city import CityRepository


class CityService:
    def __init__(self, repo: CityRepository):
        self.repo = repo

    async def create_city(
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

    async def get_city(
        self,
        db: AsyncSession,
        city_id: UUID
    ):
        return await self.repo.get(
            db,
            city_id
        )

    async def get_all_cities(
        self,
        db: AsyncSession,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str = "asc"
    ):
        return await self.repo.get_multi(
            db=db,
            search=search,
            search_fields=["city_name", "city_code"],
            order_by=(
                asc(sort_by)
                if sort_order == "asc" and sort_by
                else desc(sort_by)
                if sort_by
                else None
            )
        )

    async def get_cities_by_state(
        self,
        db: AsyncSession,
        state_id: UUID
    ):
        return await self.repo.get_by_state(
            db,
            state_id
        )

    async def update_city(
        self,
        db: AsyncSession,
        city_id: UUID,
        data: dict,
        updated_by: UUID
    ):
        return await self.repo.update(
            db,
            city_id,
            data,
            user_id=updated_by
        )

    async def delete_city(
        self,
        db: AsyncSession,
        city_id: UUID,
        deleted_by: UUID
    ):
        return await self.repo.delete(
            db,
            city_id,
            user_id=deleted_by
        )