from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
import schemas,database
from repository.user import create_user,get_user

router=APIRouter(
)

@router.post('/create_user',response_model=schemas.UserResponse,status_code=status.HTTP_201_CREATED)
def add_user(request:schemas.UserCreate,db:Session=Depends(database.get_db)):
    return create_user(request,db)

@router.get('/get_user/{user_id}',response_model=schemas.UserResponse)
def get_user(user_id,db:Session=Depends(database.get_db)):
    return get_user(user_id,db)

