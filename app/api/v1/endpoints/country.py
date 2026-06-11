from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.dependencies import get_db
from app.depedencies.country import get_country_service
from app.api.v1.schemas.masters import CountryCreate, CountryUpdate, CountryResponse
from app.services.country import CountryService

router = APIRouter(prefix="/countries", tags=["Countries"])

@router.post("/", response_model=CountryResponse)
def create_country(
    payload: CountryCreate,
    db: Session = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    return service.create_country(db, payload.dict())

@router.get("/", response_model=List[CountryResponse])
def get_countries(
    skip: int = 0, limit: int = 10,
    db: Session = Depends(get_db),
   service: CountryService = Depends(get_country_service)
):
    return service.get_all_countries(db, skip, limit)

@router.get("/{country_id}", response_model=CountryResponse)
def get_country(country_id: UUID,
    db: Session = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    return service.get_country(db, country_id)

@router.put("/{country_id}", response_model=CountryResponse)
def update_country(
    country_id: UUID,
    payload: CountryUpdate,
    db: Session = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    return service.update_country(db, country_id, payload.dict(exclude_unset=True))

@router.delete("/{country_id}", response_model=CountryResponse)
def delete_country(country_id: UUID,
    db: Session = Depends(get_db),
    service: CountryService = Depends(get_country_service)
):
    return service.delete_country(db, country_id)