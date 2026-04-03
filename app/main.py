from fastapi import FastAPI
from .database import Base, engine
from . import models
from .routes import transactions
from .routes import analytics
from .routes import users


app = FastAPI()
app.include_router(transactions.router)
app.include_router(analytics.router)
Base.metadata.create_all(bind=engine)
app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "Finance System API Running"}
