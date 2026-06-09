from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class State(BaseModel):
    __tablename__ = "states"

    state_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    state_code: Mapped[str | None] = mapped_column(
        String(10),
    )

    country_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("countries.id"),
        nullable=False,
    )