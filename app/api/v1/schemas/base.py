from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class BaseClass(BaseModel):
    id: UUID
    created_by: Optional[UUID]
    updated_by: Optional[UUID]

    created_at: datetime
    updated_at: datetime
    is_deleted: bool
