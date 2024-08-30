from fastapi import APIRouter, Depends, Request
from ..schemas import schemas
from .. import database
from sqlalchemy.orm import Session
from ..crud import user
from . import authentication 


router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/show_user', response_model=schemas.ShowUser)
def get_user(request:Request, db: Session = Depends(get_db)):
    return user.show_user(request, db)

@router.get('/login', response_model=schemas.Token)
async def login(request:Request, db: Session = Depends(get_db)):
    return await authentication.login(request, db)