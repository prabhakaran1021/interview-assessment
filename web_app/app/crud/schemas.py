from pydantic import BaseModel


class UserBase(BaseModel):
    email:str
    first_name:str
    last_name:str
    address:str
    city:str
    state:str
    pincode:int
class User(UserBase):
    id:int
    is_active:bool
    class Config:
        orm_mode=True

class UserCreate(UserBase):
    password:str


