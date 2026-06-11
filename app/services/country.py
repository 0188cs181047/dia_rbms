from sqlalchemy.orm import Session
from app.repositories.country import CountryRepository


class CountryService:
    def __init__(self, repo: CountryRepository):
        self.repo = repo

    def create_country(self, db: Session, data: dict):
        return self.repo.create(db, data)

    def get_country(self, db: Session, country_id: str):
        return self.repo.get(db, country_id)

    def get_all_countries(self, db: Session, skip=0, limit=10):
        return self.repo.get_multi(db, skip=skip, limit=limit)

    def update_country(self, db: Session, country_id: str, data: dict):
        return self.repo.update(db, country_id, data)

    def delete_country(self, db: Session, country_id: str):
        return self.repo.delete(db, country_id)

    def search_country(self, db: Session, name: str):
        return self.repo.search_country(db, name)

    def get_by_code(self, db: Session, code: str):
        return self.repo.get_by_code(db, code)