from app.repositories.module import ModuleRepository
from app.services.module import ModuleService


def get_module_repo():
    return ModuleRepository()


def get_module_service():
    return ModuleService(get_module_repo())