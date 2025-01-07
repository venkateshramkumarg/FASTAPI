from typing import List
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
import schemas,database,jwt_token,oauth2
from repository import blog

router=APIRouter(
    tags=['blog']
)

@router.post('/create_blog', response_model=schemas.BlogResponse,status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(request,db)




@router.get('/blogs/', response_model=List[schemas.BlogResponse])
def get_blogs(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blogs(db)


@router.get('/blog/{blog_id}', response_model=schemas.BlogResponse)
def get_blog(blog_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog(blog_id,db)



@router.put('/edit_blog/{blog_id}',response_model=schemas.BlogResponse,status_code=status.HTTP_202_ACCEPTED)
def edit_blog(blog_id: int, request: schemas.BlogCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.edit_blog(blog_id,request,db)


@router.delete('/blog/{blog_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id:int,db:Session=Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(blog_id,db)



