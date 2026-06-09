from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import BaseModel

class Vendor(BaseModel):
    __tablename__ = "vendors"

    vendor_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    vendor_code: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
    )

    category_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vendor_categories.id"),
        nullable=False,
    )

    owner_name: Mapped[str | None] = mapped_column(
        String(255),
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
    )

    website: Mapped[str | None] = mapped_column(
        String(500),
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    category = relationship("VendorCategory")