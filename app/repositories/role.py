from app.repositories.base import BaseRepository
from app.models.auth.role import Role


class RoleRepository(BaseRepository[Role]):
    def __init__(self):
        super().__init__(Role)
