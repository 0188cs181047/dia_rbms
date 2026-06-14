from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID

from app.api.v1.schemas.base import BaseClass

class ModuleCreate(BaseModel):
    name: str = Field(..., max_length=100)
    code: str = Field(..., max_length=50)

class ModuleUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    code: Optional[str] = Field(None, max_length=50)

class ModuleResponse(BaseClass):
    name: str
    code: str

    model_config = {
        "from_attributes": True
    }

class ModuleFilter(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None

class RoleCreate(BaseModel):
    role_name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=255)


class RoleUpdate(BaseModel):
    role_name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=255)


class RoleResponse(BaseClass):
    role_name: str
    description: Optional[str]

    model_config = {
        "from_attributes": True
    }


class RoleFilter(BaseModel):
    role_name: Optional[str] = None
    description: Optional[str] = None


class PermissionCreate(BaseModel):
    module_id: UUID
    action: str = Field(..., max_length=50)


class PermissionUpdate(BaseModel):
    module_id: Optional[UUID] = None
    action: Optional[str] = Field(None, max_length=50)


class PermissionResponse(BaseClass):
    module_id: UUID
    action: str

    model_config = {
        "from_attributes": True
    }


class PermissionFilter(BaseModel):
    module_id: Optional[UUID] = None
    action: Optional[str] = None

class RolePermissionCreate(BaseModel):
    role_id: UUID
    permission_id: UUID


class RolePermissionUpdate(BaseModel):
    role_id: Optional[UUID] = None
    permission_id: Optional[UUID] = None


class RolePermissionResponse(BaseClass):
    role_id: UUID
    permission_id: UUID

    model_config = {
        "from_attributes": True
    }


class RolePermissionFilter(BaseModel):
    role_id: Optional[UUID] = None
    permission_id: Optional[UUID] = None