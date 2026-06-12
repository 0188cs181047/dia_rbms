from sqlalchemy.orm import Session
from app.repositories.country import CountryRepository
from sqlalchemy import asc, desc
from uuid import UUID


class CountryService:
    def __init__(self, repo: CountryRepository):
        self.repo = repo

    def create_country(self, db: Session, data: dict, created_by:UUID):
        return self.repo.create(db, data, user_id=created_by)

    def get_country(self, db: Session, country_id: str):
        return self.repo.get(db, country_id)

    async def get_all_countries(
        self,
        db,
        skip=0,
        limit=10,
        search=None,
        sort_by=None,
        sort_order="asc"
    ):
        return await self.repo.get_multi(
            db=db,
            skip=skip,
            limit=limit,
            search=search,
            search_fields=["country_name", "country_code"],
            order_by=(asc(sort_by) if sort_order == "asc" and sort_by else
                      desc(sort_by) if sort_by else None)
        )

    async def update_country(self, db, country_id: UUID, data: dict, updated_by: UUID):
        return await self.repo.update(db, country_id, data, user_id=updated_by)

    async def delete_country(self, db, country_id, deleted_by):
        return await self.repo.delete(db, country_id, user_id=deleted_by)
