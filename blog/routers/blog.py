from typing import List, Union
from fastapi import APIRouter, HTTPException, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED)
async def analyze_blog(request: schemas.BlogBase, db: Session = Depends(database.get_db)):
    return await blog.analyze_blog(request, db)

@router.get('/', response_model=List[schemas.Blog])
def all(email:str, db: Session = Depends(database.get_db)):                                                                 
    return blog.get_all(email, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return blog.destroy(id,db)

@router.get('/output', response_model=List[schemas.ShowBlog])
def get_blogs_for_date(date: str, email:str, db: Session = Depends(database.get_db)):                                                                 
    return blog.get_blogs_for_date(date, email, db)

@router.get('/output_for_date_range', response_model=List[schemas.ShowBlog])
def get_blogs_for_date_range(from_date: str, to_date: str, email:str, db: Session = Depends(database.get_db)):                                                                 
    return blog.get_blogs_for_date_range(from_date, to_date, email, db)

@router.get('/classify_blog', response_model=List[schemas.ShowCategory])
async def classify_blog(date: str, email:str, db: Session = Depends(database.get_db)):
    return await blog.classify_blog(date, email, db)

@router.get('/{email}',status_code=200, response_model=schemas.ShowBlog)
def show(email: str, db:Session = Depends(get_db)):
    return blog.show(email, db)