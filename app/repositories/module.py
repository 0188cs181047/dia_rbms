from app.repositories.base import BaseRepository
from app.models.auth.module import Module


class ModuleRepository(BaseRepository[Module]):
    def __init__(self):
        super().__init__(Module)
