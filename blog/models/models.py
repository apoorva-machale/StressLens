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

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique= True)
    role_names = relationship("User", back_populates="therapist_users")
    
class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique= True)
    subscription_names = relationship("User", back_populates="premium_subscription")
    
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique= True, nullable=False)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    blogs = relationship('Blog', back_populates='creator')
    therapist_users = relationship(
        'Role',
        primaryjoin="and_(User.role_id==Role.id, Role.name=='Therapist')",
    )
    premium_subscription = relationship(
        'Subscription',
        primaryjoin="and_(User.subscription_id==Subscription.id, Subscription.name=='Premium')",
    )

class Category(Base):
    __tablename__ = 'classification'
    id = Column(Integer, primary_key=True, index=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    category_name = Column(String(255))
    category_confidence = Column(Float)
    blog_content = relationship("Blog", back_populates="classifier")


