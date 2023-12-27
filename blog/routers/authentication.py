from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas,database,models 
from .. database import get_db
from typing import List
from sqlalchemy.orm import Session
from .user import Hash

router=APIRouter(tags=["auth"])

@router.post("/login")
def login(request:schemas.Login,db:Session=Depends(get_db)):
  user=db.query(models.User).filter(models.User.email ==request.username).first()
  
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

  if not Hash.verify(user.password, request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Passwords do not match')

  return 'login'