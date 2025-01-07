from fastapi import HTTPException,status,Depends
from sqlalchemy.orm import Session
import models,hash

def create_user(request,db:Session):
    hashed_password=hash.get_password_hash(request.password)
    new_user=models.User(user_name=request.user_name,email=request.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(user_id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the id {user_id} is not found')
     
    return user

