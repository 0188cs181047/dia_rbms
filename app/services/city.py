from sqlalchemy.orm import Session
from app.repositories.city import CityRepository


class CityService:
    def __init__(self, repo: CityRepository):
        self.repo = repo

    def create_city(self, db: Session, data: dict):
        return self.repo.create(db, data)

    def get_city(self, db: Session, city_id: str):
        return self.repo.get(db, city_id)
    
    def get_all_cities(self, db: Session, skip: int = 0, limit: int = 10):
        return self.repo.get_multi(db, skip=skip, limit=limit)


    def get_cities_by_state(self, db: Session, state_id: str):
        return self.repo.get_by_state(db, state_id)

    def update_city(self, db: Session, city_id: str, data: dict):
        return self.repo.update(db, city_id, data)

    def delete_city(self, db: Session, city_id: str):
        return self.repo.delete(db, city_id)

    def search_city(self, db: Session, name: str):
        return self.repo.search_city(db, name)