from app.repositories.permission import PermissionRepository
from app.services.permission import PermissionService


def get_permission_repo():
    return PermissionRepository()


def get_permission_service():
    return PermissionService(get_permission_repo())