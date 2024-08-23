from fastapi import APIRouter, Depends, Header
from ..schemas import schemas
from .. import database
from sqlalchemy.orm import Session
from ..crud import user
from . import authentication 
from ..utils.token_login import verify_token

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.post('/user_details', response_model=schemas.ShowUser)
async def get_user_details(request: schemas.UserEmail, Token:str= Header(), db: Session = Depends(get_db)):
    current_user_email = await verify_token(Token)
    return await user.show_user(request, current_user_email, db)

@router.post('/login', response_model=schemas.Token)
async def login(request:schemas.Login, db: Session = Depends(get_db)):
    return await authentication.login(request, db)