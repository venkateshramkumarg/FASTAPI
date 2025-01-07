from fastapi import APIRouter,Depends,status
import schemas,database
from sqlalchemy.orm import Session
from repository import user


router=APIRouter(
    tags=['user']
)

@router.post('/create_user',response_model=schemas.UserResponse,status_code=status.HTTP_201_CREATED)
def add_user(request:schemas.UserCreate,db:Session=Depends(database.get_db)):
    return user.create_user(request,db)

@router.get('/get_user/{user_id}',response_model=schemas.UserResponse)
def get_user(user_id,db:Session=Depends(database.get_db)):
    return user.get_user(user_id,db)

@router.post('/check_user',status_code=status.HTTP_200_OK)
def check_user(request:schemas.UserCreate,db:Session=Depends(database.get_db)):
    return user.check_user(request,db)