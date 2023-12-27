from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, models
from .. database import get_db
from typing import List
from sqlalchemy.orm import Session

router=APIRouter(tags=["blogs"])


#Get All request
@router.get("/blog", response_model=List[schemas.showClass])
def all(db:Session=Depends(get_db)):
  gt_blog=db.query(models.Blog).all()
  return gt_blog

#Post request
@router.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db:Session=Depends(get_db)):
  new_blog=models.Blog(title=request.title, body=request.body, user_id=1 )
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

#Get a single item
#Custom error response
@router.get("/blog/{id}", response_model=schemas.showClass)
def show(id:int,response:Response, db:Session=Depends(get_db)):
  gt_blog=db.query(models.Blog).filter(models.Blog.id==id).first()

  if not gt_blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The blog with {id} not found')
  return gt_blog

#delete request
@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session=Depends(get_db)):
  del_blog= db.query(models.Blog).filter(models.Blog.id==id)

  #if blog isn't there
  if not del_blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id: {id} not found')
  del_blog.delete(synchronize_session=False)
  db.commit()
  return "done" 

#Update request
@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session=Depends(get_db)):
  up_blog=db.query(models.Blog).filter(models.Blog.id==id)

  #if blog isn't there
  if not up_blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id:{id} not found')
  
  up_blog.update({'title': request.title, 'body': request.body})
  db.commit()
  return "updated"

####return a dict instead of string