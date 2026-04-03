from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    note: str


class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    role: str  # viewer, analyst, admin


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True        