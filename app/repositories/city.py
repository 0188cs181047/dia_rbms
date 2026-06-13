from app.repositories.base import BaseRepository
from app.models.masters.city import City
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CityRepository(BaseRepository[City]):
    def __init__(self):
        super().__init__(City)

    async def get_by_state(self, db: AsyncSession, state_id: str):
        stmt = select(self.model).where(
            self.model.state_id == state_id,
            self.model.is_deleted.is_(False)
        )

        result = await db.execute(stmt)

        return result.scalars().all()
