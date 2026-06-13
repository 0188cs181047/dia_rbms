from sqlalchemy.orm import Session
from app.repositories.state import StateRepository
from uuid import UUID
from sqlalchemy import asc, desc
from sqlalchemy.ext.asyncio import AsyncSession


class StateService:
    def __init__(self, repo: StateRepository):
        self.repo = repo

    def create_state(self, db: Session, data: dict, created_by:UUID):
        return self.repo.create(db, data, user_id=created_by )

    async def get_state(self, db: Session, state_id: UUID):
        return await self.repo.get(db, state_id)
    
    async def get_all_states(
        self,
        db,
        search=None,
        sort_by=None,
        sort_order="asc"
    ):
        return await self.repo.get_multi(
            db=db,
            search=search,
            search_fields=["state_name", "state_code"],
            order_by=(asc(sort_by) if sort_order == "asc" and sort_by else
                      desc(sort_by) if sort_by else None)
        )

    async def get_states_by_country(
        self,
        db: AsyncSession,
        country_id: UUID
    ):
        return await self.repo.get_by_country(db, country_id)

    async def update_state(self, db: Session, state_id: str, data: dict, updated_by):
        return await self.repo.update(db, state_id, data, user_id=updated_by)

    async def delete_state(self, db: Session, state_id: str, deleted_by):
        return await self.repo.delete(db, state_id, user_id=deleted_by)
