from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creation_time = Column(Date)
    updation_time = Column(Date)
    analysis = Column(String)
    sentiment_score = Column(Float)
    sentiment_magnitude = Column(Float)
    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique= True, nullable=False)
    password = Column(String, nullable=False)
    blogs = relationship('Blog', back_populates='creator')


