from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
  title:str
  body:str

class Blog(BlogBase):
  class Config:
    orm_mode=True

class newUser(BaseModel):
  name:str
  email:str
  password:str

class showUser(BaseModel):
  name:str
  email:str
  blogs:List[Blog]=[]
  class Config:
    orm_mode=True

class showClass(Blog):
  title:str
  body:str
  creator:showUser
  class Config:
    orm_mode=True

class Login(BaseModel):
  username:str
  password:str
