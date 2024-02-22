from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    body: str
    class Config():
        from_attributes = True

class Blog(BlogBase):
    class Config():
        from_attributes = True
        
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    

class ShowBlog(Blog):
    title: str
    creator: ShowUser
    class Config():
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str



