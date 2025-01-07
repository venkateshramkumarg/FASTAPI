from fastapi import HTTPException,status
from sqlalchemy.orm import Session
import schemas,hash,models,jwt_token,hash
from datetime import datetime, timedelta, timezone

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

def check_user(request:schemas.UserCreate,db:Session):
    user=db.query(models.User).filter(models.User.email==request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User with email {request.email} is not found')
    
    if not hash.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Incorrect password')
    
    access_token_expires = timedelta(minutes=jwt_token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt_token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token":access_token, "token_type":"bearer"}