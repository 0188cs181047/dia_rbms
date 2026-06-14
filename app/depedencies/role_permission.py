from app.repositories.role_permission import RolePermissionRepository
from app.services.role_permission import RolePermissionService


def get_role_permission_repo():
    return RolePermissionRepository()


def get_role_permission_service():
    return RolePermissionService(get_role_permission_repo())