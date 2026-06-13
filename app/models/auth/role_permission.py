from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class RolePermission(BaseModel):
    __tablename__ = "role_permissions"

    role_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("roles.id"),
        nullable=False,
    )

    permission_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("permissions.id"),
        nullable=False,
    )