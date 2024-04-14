from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from datetime import datetime
from sentiment import sentiment_analysis_label

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def analyze_blog(request: schemas.Blog, db: Session):
    output = sentiment_analysis_label(request.body)
    new_blog = models.Blog(title=request.title, body= request.body,user_id=1, creation_time=datetime.now(), analysis= output['analysis'], sentiment_score = output['sentiment_score'], sentiment_magnitude = output['sentiment_magnitude'])
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Done'

# def update(email, request: schemas.Blog, db: Session):
#     blog = db.query(models.Blog).filter(models.Blog.email==email)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with email {id} not found")
#     output = sentiment_analysis_label(request.body)
#     blog.update(title=request.title, body= request.body, user_id=1, updation_time=datetime.now(), analysis= output['analysis'], sentiment_score = output['sentiment_score'], sentiment_magnitude = output['sentiment_magnitude'])
#     db.commit()
#     return 'updated successfully'

def get_blogs_for_date(date, db: Session):
    print("date",date)
    blog = db.query(models.Blog).filter(models.Blog.creation_time == date)
    print("blog",blog)
    return blog
    
def show(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available")
    return blog
    