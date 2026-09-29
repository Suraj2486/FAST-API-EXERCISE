from pydantic import BaseModel, EmailStr
from datetime import datetime

from app.db import Base

class PostBase(BaseModel):
    name: str
    age: int
    published: bool = True

class PostCreate(PostBase):
    pass 

class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode : True

class User(BaseModel):
    email : EmailStr
    pw : str

class Userout(BaseModel):
    id: int
    email :EmailStr

    class COnfig:
        orm_mode : True