from app.repositories.base import BaseRepository
from app.models.masters.state import State
from sqlalchemy import select
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession


class StateRepository(BaseRepository[State]):
    def __init__(self):
        super().__init__(State)

    async def get_by_country(self, db: AsyncSession, country_id: UUID):
        stmt = select(self.model).where(
            self.model.country_id == country_id,
            self.model.is_deleted == False
        )

        result = await db.execute(stmt)

        return result.scalars().all()