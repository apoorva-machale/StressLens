from sqlalchemy.orm import Session

from ..models import models
from ..schemas import schemas
from fastapi import HTTPException, status
from datetime import datetime
from blog.dependencies.sentiment import sentiment_analysis_label
from blog.dependencies.classify_text import classify_text
from .user import show_user

def get_all(email, db: Session):
    print(email)
    try:
        user = db.query(models.User).filter(models.User.email == email).first()
        print("USER",user)
        print("check",user is None)
        if user is None:
            return []
        else:
            # print("hi")
            blogs = db.query(models.Blog).filter(models.Blog.user_id == user.id).all()
            return blogs
    except Exception as e:
        # print("hello")
        print(f"Error classifying blog: {e}")
        return None
    

async def analyze_blog(request: schemas.BlogBase, email, db: Session):
    try:
        user = db.query(models.User).filter(
            models.User.email == email
        ).first()
        # print("user",user)
        if user:
            # print("request.body",request.body)
            word_count = len(request.body.split())
            if word_count < 25:
                return "Insufficient word count to classify the blog"
            else:
                sentiment_output = sentiment_analysis_label(request.body)
                # print("sentiment_output",sentiment_output)
                _id = user.id
                # print("user_id",_id)
                sentiment_blog = models.Blog(title=request.title, body= request.body, user_id=_id, creation_time=datetime.now(), analysis= sentiment_output['analysis'], sentiment_score = sentiment_output['sentiment_score'], sentiment_magnitude = sentiment_output['sentiment_magnitude'])
                # print("new blog1", sentiment_blog)
                db.add(sentiment_blog)
                db.commit()
                db.refresh(sentiment_blog)
                classifier_output = classify_text(request.body)
                # print("classifier_output ----",classifier_output)
                for category in classifier_output:
                    category = models.Category(blog_id = sentiment_blog.id, category_name = category['category_name'], category_confidence = category['category_confidence'])
                    db.add(category)
                    db.commit()
                    db.refresh(category)
                return classifier_output
    except Exception as e:
        print(f"Error classifying blog: {e}")
        return None

async def classify_blog(date, email, db: Session):
    try:
        user = db.query(models.User).filter(
            models.User.email == email
        ).first()
        print(user.id)
        if user:
            blog = db.query(models.Blog).filter(
            models.Blog.creation_time == date,
            models.Blog.user_id == user.id).first()
            if blog is not None:
                classification = db.query(models.Category).filter(
                    models.Category.blog_id == blog.id
                ).all()
                return classification
            else:
                print("Blog not found for the given date")
                return []
        else:
            print("User not found for the given email")
    except Exception as e:
        print(f"Error classifying blog: {e}")
        return None

async def classify_blog_id(blog_id, db: Session):
    try:
        classification = db.query(models.Category).filter(
            models.Category.blog_id == blog_id
        ).all()
        return classification
    except Exception as e:
        print(f"Error classifying blog: {e}")
        return None

def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    print('Blog deleted')
    return 'Blog deleted'

def get_blogs_for_date_range(from_date, to_date, email, db: Session):
    # print("date",date)
    user = db.query(models.User).filter(models.User.email == email).first()
    _id = user.id
    # print("id--------------------------------------------------------------",_id)
    blog = db.query(models.Blog).filter(models.Blog.creation_time.between(from_date, to_date), models.Blog.user_id == _id)
    # print("blog",blog)
    return blog

def get_blogs_for_date(date, email, db: Session):
    # print("date",date)
    user = db.query(models.User).filter(models.User.email == email).first()
    _id = user.id
    # print("id--------------------------------------------------------------",_id)
    blog = db.query(models.Blog).filter(models.Blog.creation_time == date, models.Blog.user_id == _id)
    # print("blog",blog)
    return blog
    
def show(email, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    _id = user.id
    blog = db.query(models.Blog).filter(models.Blog.user_id == user.id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog
    