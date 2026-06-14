from app.repositories.base import BaseRepository
from app.models.auth.permission import Permission


class PermissionRepository(BaseRepository[Permission]):
    def __init__(self):
        super().__init__(Permission)
