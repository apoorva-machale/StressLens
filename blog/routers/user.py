from fastapi import APIRouter, Depends

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

@router.get('/{email}', response_model=schemas.ShowUser)
def get_user(email:str, db: Session = Depends(get_db)):
    return user.show_user(email, db)

@router.post('/login', response_model=schemas.Token)
async def login(request:schemas.Login, db: Session = Depends(get_db)):
    return await authentication.login(request, db)