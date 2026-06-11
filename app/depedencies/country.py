from app.repositories.country import CountryRepository
from app.services.country import CountryService


def get_country_repo():
    return CountryRepository()


def get_country_service():
    return CountryService(get_country_repo())