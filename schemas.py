from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    author_id: int

class UserBase(BaseModel):
    user_name: str
    email: str

class UserResponse(BaseModel):
    id: int
    user_name: str
    email: str
    blogs: List[BlogBase]
    class Config:
        from_attributes = True 

class BlogResponse(BlogBase):
    id: int
    author: UserBase|None=None

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str
    pass




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str