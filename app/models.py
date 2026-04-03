from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    role = Column(String)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String)  # income / expense
    category = Column(String)
    date = Column(Date)
    note = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))