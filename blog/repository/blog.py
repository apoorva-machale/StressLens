from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from datetime import datetime
from sentiment import sentiment_analysis_label
from classify_text import classify_text
from .user import show_user

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def analyze_blog(request: schemas.Blog, db: Session):
    sentiment_output = sentiment_analysis_label(request.body)
   
    user = db.query(models.User).filter(models.User.email == request.email).first()
    _id = user.id
    sentiment_blog = models.Blog(title=request.title, body= request.body, user_id=_id, creation_time=datetime.now(), analysis= sentiment_output['analysis'], sentiment_score = sentiment_output['sentiment_score'], sentiment_magnitude = sentiment_output['sentiment_magnitude'])
    print("new blog1", sentiment_blog)
    db.add(sentiment_blog)
    db.commit()
    db.refresh(sentiment_blog)
    word_count = len(request.body.split())
    if word_count < 25:
        return "Insufficient word count"
    else:
        classifier_output = classify_text(request.body)
        print("classifier_output ----",classifier_output)
        for category in classifier_output:
            new_blog = models.Classifier(blog_id = sentiment_blog.id, category_name = category['category_name'], category_confidence = category['category_confidence'])
            db.add(new_blog)
            db.commit()
            db.refresh(new_blog)
    return new_blog

def classify_blog(date, db: Session):
    print("date",date)
    blog = db.query(models.Blog).filter(models.Blog.creation_time == date)
    classification = db.query(models.Classifier).filter(models.Classifier.blog_id == blog.id)
    print("classification",classification)
    return classification

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

def get_blogs_for_date(date, email, db: Session):
    print("date",date)
    user = db.query(models.User).filter(models.User.email == email).first()
    _id = user.id
    print("id--------------------------------------------------------------",_id)
    blog = db.query(models.Blog).filter(models.Blog.creation_time == date, models.Blog.user_id == _id)
    print("blog",blog)
    return blog
    
def show(email, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    _id = user.id
    blog = db.query(models.Blog).filter(models.Blog._id == user.id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog
    