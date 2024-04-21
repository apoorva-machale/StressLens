from typing import List, Union
from fastapi import APIRouter, HTTPException, Depends, status,Header,Request
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog
from ..token_login import verify_token


router = APIRouter(
    prefix="/blog",
    tags=['Blogs'],
    
    
)
get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED)
async def analyze_blog(request_body: schemas.BlogBase, Token:str= Header() ,db: Session = Depends(database.get_db)):
    print("This is Headerrrr",Token)
    email = await verify_token(Token)
    return await blog.analyze_blog(request_body, email, db)

@router.get('/', response_model=List[schemas.Blog])
async def get_all(db: Session = Depends(database.get_db), Token:str= Header()): 
    print("This is Headerrrr Autho",Token)
    email = await verify_token(Token)
    print("email",email)                                 
    return blog.get_all(email, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    # print("This is Headerrrr Autho",test_h)
    # email = await verify_token(test_h)
    return blog.destroy(id, db)

@router.get('/output', response_model=List[schemas.ShowBlog])
async def get_blogs_for_date(date: str,db: Session = Depends(database.get_db),Token:str= Header()):                                                                 
    print("This is Headerrrr Autho",Token)
    email= await verify_token(Token)
    return blog.get_blogs_for_date(date, email, db)

@router.get('/output_for_date_range', response_model=List[schemas.ShowBlog])
async def get_blogs_for_date_range(from_date: str, to_date: str,
                              db: Session = Depends(database.get_db), Token:str= Header()):                                                                 
    print("This is Headerrrr Autho",Token)
    email= await verify_token(Token)
    return blog.get_blogs_for_date_range(from_date, to_date, email, db)

@router.get('/classify_blog', response_model=List[schemas.ShowCategory])
async def classify_blog(date: str, db: Session = Depends(database.get_db),Token:str= Header()):
    print("This is Headerrrr Autho",Token)
    email= await verify_token(Token)
    return await blog.classify_blog(date, email, db)

@router.get('/classify_blog_id', response_model=List[schemas.ShowCategory])
async def classify_blog_id(blog_id:int, db: Session = Depends(database.get_db),Token:str= Header()):
    print("This is Headerrrr Autho",Token)
    # email= await verify_token(test_h)
    return await blog.classify_blog_id(blog_id, db)

@router.get('/{email}',status_code=200, response_model=schemas.ShowBlog)
async def show(Token:str= Header(), db:Session = Depends(get_db)):
    print("This is Headerrrr Autho",Token)
    email= await verify_token(Token)
    return await blog.show(email, db)