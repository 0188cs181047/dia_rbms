from app.repositories.base import BaseRepository
from app.models.masters.city import City


class CityRepository(BaseRepository[City]):
    def __init__(self):
        super().__init__(City)

    def get_by_state(self, db, state_id: str):
        return db.query(self.model).filter(
            self.model.state_id == state_id,
            self.model.is_deleted == False
        ).all()

    def get_by_country(self, db, country_id: str):
        return db.query(self.model).join(self.model.state).filter(
            self.model.state.has(country_id=country_id),
            self.model.is_deleted == False
        ).all()

    def search_city(self, db, name: str):
        return self.search(db, "city_name", name)