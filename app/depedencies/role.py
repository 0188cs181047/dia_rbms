from app.repositories.role import RoleRepository
from app.services.role import RoleService


def get_role_repo():
    return RoleRepository()


def get_role_service():
    return RoleService(get_role_repo())