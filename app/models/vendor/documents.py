from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseModel

class VendorDocument(BaseModel):
    __tablename__ = "vendor_documents"

    vendor_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vendors.id"),
        nullable=False,
    )

    document_type: Mapped[str] = mapped_column(
        String(100),
    )

    document_name: Mapped[str] = mapped_column(
        String(255),
    )

    file_url: Mapped[str] = mapped_column(
        String(1000),
    )