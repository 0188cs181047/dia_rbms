from app.repositories.base import BaseRepository
from app.models.masters.country import Country


class CountryRepository(BaseRepository[Country]):
    def __init__(self):
        super().__init__(Country)
