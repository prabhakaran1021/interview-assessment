from app.database import Base
from sqlalchemy import String, Integer, Column, Boolean


class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String(64),unique=True,index=True)
    password=Column(String(64))
    first_name=Column(String(64))
    last_name=Column(String(64))
    address=Column(String(64))
    city=Column(String(64))
    state=Column(String(64))
    pincode=Column(Integer)
    is_active=Column(Boolean,default=True)


