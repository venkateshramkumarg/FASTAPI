from typing import Annotated
from fastapi import HTTPException,Depends,status
from fastapi.security import OAuth2PasswordBearer
import jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return jwt_token.verify_token(token,credentials_exception)
