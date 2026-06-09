from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class City(BaseModel):
    __tablename__ = "cities"

    city_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    state_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("states.id"),
        nullable=False,
    )