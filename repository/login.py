

def check_user(request,db:Session):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with email {request.username} is not found')
    
    if not hash.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Incorrect password')
    
    access_token_expires = timedelta(minutes=jwt_token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt_token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token":access_token, "token_type":"bearer"}