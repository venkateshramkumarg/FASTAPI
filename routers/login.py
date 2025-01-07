from fastapi import APIRoute,Depends,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import database
from repository import login

router=APIRoute()


@router.post('/token', status_code=status.HTTP_200_OK)
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return login.check_user (request,db)