from app.repositories.base import BaseRepository
from app.models.masters.state import State


class StateRepository(BaseRepository[State]):
    def __init__(self):
        super().__init__(State)

    def get_by_country(self, db, country_id: str):
        return db.query(self.model).filter(
            self.model.country_id == country_id,
            self.model.is_deleted == False
        ).all()

    def get_by_code(self, db, code: str):
        return db.query(self.model).filter(
            self.model.state_code == code,
            self.model.is_deleted == False
        ).first()

    def search_state(self, db, name: str):
        return self.search(db, "state_name", name)