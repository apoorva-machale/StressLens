from typing import List
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
def analyze_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.analyze_blog(request, db)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):                                                                 
    return blog.get_all(db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id,db)

@router.get('/output', response_model=List[schemas.ShowBlog])
def get_blogs_for_date(date: str, db: Session = Depends(database.get_db)):                                                                 
    return blog.get_blogs_for_date(date,db)
# @router.put('/{email}', status_code=status.HTTP_202_ACCEPTED)
# def update(email: str, request: schemas.Blog, db: Session = Depends(get_db)):
#    return blog.update(email, db)

@router.post('/classify_blog', status_code=status.HTTP_201_CREATED)
def classify_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.classify_blog(request, db)

@router.get('/{id}',status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db:Session = Depends(get_db)):
    return blog.show(id, db)