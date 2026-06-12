from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class CountryCreate(BaseModel):
    country_name: str = Field(..., max_length=100)
    country_code: str = Field(..., max_length=10)


class CountryUpdate(BaseModel):
    country_name: Optional[str] = Field(None, max_length=100)


class CountryResponse(BaseModel):
    id: UUID
    country_name: str
    country_code: str

    created_by: Optional[UUID]
    updated_by: Optional[UUID]

    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    model_config = {
        "from_attributes": True
    }

class CountryFilter(BaseModel):
    country_name: Optional[str] = None
    country_code: Optional[str] = None


class CityCreate(BaseModel):
    city_name: str = Field(..., max_length=100)
    state_id: UUID

class CityUpdate(BaseModel):
    city_name: Optional[str] = Field(None, max_length=100)
    state_id: Optional[UUID] = None

class CityResponse(BaseModel):
    id: UUID
    city_name: str
    state_id: UUID

    created_by: Optional[UUID]
    updated_by: Optional[UUID]

    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    class Config:
        from_attributes = True

class StateCreate(BaseModel):
    state_name: str = Field(..., max_length=100)
    state_code: Optional[str] = Field(None, max_length=10)
    country_id: UUID

class StateUpdate(BaseModel):
    state_name: Optional[str] = Field(None, max_length=100)
    state_code: Optional[str] = Field(None, max_length=10)
    country_id: Optional[UUID] = None

class StateResponse(BaseModel):
    id: UUID
    state_name: str
    state_code: Optional[str]
    country_id: UUID

    created_by: Optional[UUID]
    updated_by: Optional[UUID]

    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    class Config:
        from_attributes = True
        
class StateFilter(BaseModel):
    state_name: Optional[str] = None
    state_code: Optional[str] = None
    country_id: Optional[UUID] = None