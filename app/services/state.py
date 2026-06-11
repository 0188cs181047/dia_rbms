from sqlalchemy.orm import Session
from app.repositories.state import StateRepository


class StateService:
    def __init__(self, repo: StateRepository):
        self.repo = repo

    def create_state(self, db: Session, data: dict):
        return self.repo.create(db, data)

    def get_state(self, db: Session, state_id: str):
        return self.repo.get(db, state_id)

    def get_states_by_country(self, db: Session, country_id: str):
        return self.repo.get_by_country(db, country_id)

    def update_state(self, db: Session, state_id: str, data: dict):
        return self.repo.update(db, state_id, data)

    def delete_state(self, db: Session, state_id: str):
        return self.repo.delete(db, state_id)

    def search_state(self, db: Session, name: str):
        return self.repo.search_state(db, name)