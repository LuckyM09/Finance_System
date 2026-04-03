from fastapi import Header, HTTPException
from ..database import SessionLocal
from .. import models

def get_current_user(username: str = Header(...)):
    db = SessionLocal()
    user = db.query(models.User).filter(models.User.username == username).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

def require_admin(user):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")