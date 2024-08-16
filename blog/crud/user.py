from sqlalchemy.orm import Session

from ..schemas import schemas

from ..models import models
from .. import database
from fastapi import HTTPException, status, Depends
from ..utils.hashing import Hash

def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    email_check = db.query(models.User).filter(models.User.email ==request.email).first()
    if email_check != None:
       raise HTTPException(detail='Email is already registered', status_code= status.HTTP_409_CONFLICT)
    else: 
        new_user = models.User(name =request.name,email =request.email,password=Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

def show_user(email: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the email {email} is not available")
    return user