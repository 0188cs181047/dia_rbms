from app.repositories.city import CityRepository
from app.services.city import CityService


def get_city_repo():
    return CityRepository()


def get_city_service():
    return CityService(get_city_repo())