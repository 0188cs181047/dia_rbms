from app.repositories.base import BaseRepository
from app.models.auth.role_permission import RolePermission


class RolePermissionRepository(BaseRepository[RolePermission]):
    def __init__(self):
        super().__init__(RolePermission)
