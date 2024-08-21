from pydantic import BaseModel, EmailStr
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str
    class Config():
        from_attributes = True

class Blog(BaseModel):
    id: int
    title: str
    body: str
    class Config():
        from_attributes = True
        
class ShowUser(BaseModel):
    name: str
    email: EmailStr
    blogs: List[Blog]
    
class SuggestionBlog(BaseModel):
    suggestions: str

class ShowBlog(Blog):
    analysis: str
    sentiment_score: float
    sentiment_magnitude: float
    class Config():
        from_attributes = True

class Category(BaseModel):
    category_name: str
    category_confidence: float
    class Config():
        from_attributes = True

class ShowCategory(BaseModel):
    blog_id: int
    category_name: str
    category_confidence: float
    class Config():
        from_attributes = True

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None




