from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.db.dependencies import get_db
from app.depedencies.city import get_city_service
from app.api.v1.schemas.masters import CityCreate, CityResponse, CityUpdate
from app.services.city import CityService

router = APIRouter(prefix="/cities", tags=["Cities"])

@router.post("/", response_model=CityResponse)
def create_city(
    payload: CityCreate,
    db: Session = Depends(get_db),
    service:CityService = Depends(get_city_service)
):
    return service.create_city(db, payload.dict())

@router.get("/",  response_model=List[CityResponse])
def get_cities(skip: int = 0, limit: int = 10,
    db: Session = Depends(get_db),
    service:CityService = Depends(get_city_service)
):
    return service.get_all_cities(db, skip, limit)

@router.get("/state/{state_id}",  response_model=CityResponse)
def get_cities_by_state(state_id: UUID,
    db: Session = Depends(get_db),
    service:CityService = Depends(get_city_service)
):
    return service.get_cities_by_state(db, state_id)

@router.get("/{city_id}", response_model=CityResponse)
def get_city(city_id: UUID,
    db: Session = Depends(get_db),
    service:CityService = Depends(get_city_service)
):
    return service.get_city(db, city_id)


@router.put("/{city_id}", response_model=CityResponse)
def update_city(city_id: UUID,
    payload: CityUpdate,
    db: Session = Depends(get_db),
    service:CityService = Depends(get_city_service)
):
    return service.update_city(db, city_id, payload)

@router.delete("/{city_id}", response_model=CityResponse)
def delete_city(city_id: UUID,
    db: Session = Depends(get_db),
    service:CityService = Depends(get_city_service)
):
    return service.delete_city(db, city_id)