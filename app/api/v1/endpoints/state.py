from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.db.dependencies import get_db
from app.depedencies.state import get_state_service
from app.api.v1.schemas.masters import StateCreate, StateUpdate, StateResponse
from app.services.state import StateService

router = APIRouter(prefix="/states", tags=["States"])

@router.post("/", response_model=StateResponse)
def create_state(
    payload: StateCreate,
    db: Session = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    return service.create_state(db, payload.dict())

@router.get("/", response_model=List[StateResponse])
def get_states(skip: int = 0, limit: int = 10,
    db: Session = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    return service.get_all_states(db, skip, limit)

@router.get("/country/{country_id}", response_model=StateResponse)
def get_states_by_country(country_id: UUID,
    db: Session = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    return service.get_states_by_country(db, country_id)

@router.get("/{state_id}", response_model=StateResponse)
def get_state(state_id: UUID,
    db: Session = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    return service.get_state(db, state_id)


@router.put("/{state_id}", response_model=StateResponse)
def update_state(
    state_id: UUID,
    payload: StateUpdate,
    db: Session = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    return service.update_state(db, state_id, payload.dict(exclude_unset=True))


@router.delete("/{state_id}", response_model=StateResponse)
def delete_state(state_id: UUID,
    db: Session = Depends(get_db),
    service:StateService = Depends(get_state_service)
):
    return service.delete_state(db, state_id)