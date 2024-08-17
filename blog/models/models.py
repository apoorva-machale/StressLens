from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from ..database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    body = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    creation_time = Column(Date)
    analysis = Column(String(255))
    sentiment_score = Column(Float)
    sentiment_magnitude = Column(Float)
    creator = relationship("User", back_populates="blogs")
    classifier = relationship("Category", back_populates="blog_content")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique= True, nullable=False)
    password = Column(String(255), nullable=False)
    blogs = relationship('Blog', back_populates='creator')

class Category(Base):
    __tablename__ = 'classification'
    id = Column(Integer, primary_key=True, index=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    category_name = Column(String(255))
    category_confidence = Column(Float)
    blog_content = relationship("Blog", back_populates="classifier")


