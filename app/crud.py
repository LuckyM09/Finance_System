from sqlalchemy.orm import Session
from . import models, schemas

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        amount=transaction.amount,
        type=transaction.type,
        category=transaction.category,
        date=transaction.date,
        note=transaction.note,
        user_id=1   # temporary
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_transactions(db: Session):
    return db.query(models.Transaction).all()

def update_transaction(db, transaction_id, updated_data):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()

    if not transaction:
        return None

    for key, value in updated_data.dict().items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)
    return transaction

def delete_transaction(db, transaction_id):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()

    if not transaction:
        return None

    db.delete(transaction)
    db.commit()
    return {"message": "Deleted successfully"}

def filter_transactions(db, type=None, category=None, start_date=None, end_date=None):
    query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)

    if category:
        query = query.filter(models.Transaction.category == category)

    if start_date:
        query = query.filter(models.Transaction.date >= start_date)

    if end_date:
        query = query.filter(models.Transaction.date <= end_date)

    return query.all()

def create_user(db, user):
    db_user = models.User(
        username=user.username,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db):
    return db.query(models.User).all()