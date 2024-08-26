from sqlalchemy.orm import Session
from ..schemas import schemas
from ..models import models
from .. import database
from fastapi import HTTPException, status, Depends

def is_therapist(email: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Therapist with the email {email} is not available")
    therapist = db.query(models.User).filter(models.User.email == email, models.User.therapist_users).first()
    if bool(therapist):
        return True
    return False

def is_premium(email: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the email {email} is not available")
    premium = db.query(models.User).filter(models.User.email == email, models.User.premium_subscription).first()
    if bool(premium):
        return True
    return False