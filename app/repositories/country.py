from app.repositories.base import BaseRepository
from app.models.masters.country import Country


class CountryRepository(BaseRepository[Country]):
    def __init__(self):
        super().__init__(Country)

    def get_by_code(self, db, code: str):
        return db.query(self.model).filter(
            self.model.country_code == code,
            self.model.is_deleted == False
        ).first()

    def search_country(self, db, name: str):
        return self.search(db, "country_name", name)