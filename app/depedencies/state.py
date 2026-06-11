from app.repositories.state import StateRepository
from app.services.state import StateService


def get_state_repo():
    return StateRepository()


def get_state_service():
    return StateService(get_state_repo())