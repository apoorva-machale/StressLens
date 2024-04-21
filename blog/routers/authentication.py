from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, models, token_login, schemas
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

async def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    print(request)
    print(type(request))
    try:
        user = db.query(models.User).filter(models.User.email == request.username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials") 
        if not Hash.verify(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password") 
        access_token = token_login.create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        print(f"Error while login: {e}")
        return None