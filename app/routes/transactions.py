from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..database import SessionLocal
from .. import crud, schemas
from ..utils.dependencies import get_current_user, require_admin

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/transactions")
def create(
    transaction: schemas.TransactionCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    require_admin(user)
    return crud.create_transaction(db, transaction)


@router.get("/transactions")
def read_all(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return crud.get_transactions(db)

@router.put("/transactions/{id}")
def update(id: int, transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    updated = crud.update_transaction(db, id, transaction)
    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated

@router.delete("/transactions/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    require_admin(user)
    return crud.delete_transaction(db, id)

from typing import Optional
from datetime import date

@router.get("/transactions/filter")
def filter_data(
    type: Optional[str] = None,
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    return crud.filter_transactions(db, type, category, start_date, end_date)