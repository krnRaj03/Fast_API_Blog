from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, models
from .. database import get_db
from typing import List
from sqlalchemy.orm import Session
#for hashing pass
from passlib.context import CryptContext

router=APIRouter()

#for password hashing
pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")

#for creating user
@router.post("/user", response_model=schemas.showUser,tags=["users"])
def create_user(request:schemas.newUser,db:Session=Depends(get_db)):
  hashedPassword=pwd_cxt.hash(request.password)
  cr_user=models.User(name=request.name, email=request.email, password=hashedPassword)
  db.add(cr_user)
  db.commit()
  db.refresh(cr_user)
  return cr_user

#getting user
@router.get("/user/{id}",tags=["users"])
def get_user(id:int,response:Response, db:Session=Depends(get_db)):
  gt_user=db.query(models.User).filter(models.User.id==id).first()

  if not gt_user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The User with id:{id} not found')
  return gt_user

class Hash():
  def bcrypt(password:str):
    return pwd_cxt.hash(password)

  def verify(hashed_password, plain_password):
    return pwd_cxt.verify(hashed_password, plain_password)