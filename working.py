from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()


##Query parameters
@app.get("/blog")
def home(limit:int=10,published:bool=True, sort: Optional[str]=None):
  # return published
  if  published:
    x={'data':f'{limit} published blogs from the db'}
    return x
  else:
    y={'data':f'{limit} blogs from the db'}
    return y


@app.get("/blog/unpublished")
def show1():
  return {'data':"all unpublished blogs"}


@app.get("/blog/{id}")
def show(id:int):
  return {'data':id}

@app.get("/blog/{id}/comments")
def comments(id,limit=10):
  return {'data':{1,2}}

class Blog(BaseModel):
  title:str
  body:str
  published:Optional[bool]


@app.post("/blog")
def create_blog(request:Blog):
  return {'data':f'Blog title is {request.title} & body is {request.body}'}
