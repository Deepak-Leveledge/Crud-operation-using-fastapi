from sqlalchemy import Column, Integer, String,Boolean
# models.py
from .database import Base 


# User table model
class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    email=Column(String,unique=True,index=True)
    password=Column(String)
    is_active=Column(Boolean,default=True)