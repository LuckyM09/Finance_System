from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import extract
from ..database import SessionLocal
from .. import models

router = APIRouter(prefix="/analytics")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total_income = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "income"
    ).scalar() or 0

    total_expense = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "expense"
    ).scalar() or 0

    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }

@router.get("/category")
def category_breakdown(db: Session = Depends(get_db)):
    data = db.query(
        models.Transaction.category,
        func.sum(models.Transaction.amount)
    ).group_by(models.Transaction.category).all()

    return [{"category": c, "total": t} for c, t in data]



@router.get("/monthly")
def monthly_summary(db: Session = Depends(get_db)):
    data = db.query(
        extract('month', models.Transaction.date),
        func.sum(models.Transaction.amount)
    ).group_by(extract('month', models.Transaction.date)).all()

    return [{"month": int(m), "total": t} for m, t in data]