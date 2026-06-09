from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class Country(BaseModel):
    __tablename__ = "countries"

    country_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    country_code: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
    )