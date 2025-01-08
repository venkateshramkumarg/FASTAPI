from typing import List
from fastapi import APIRouter, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session
import schemas, database, oauth2
from email_service import  send_email
from repository.blog import (
    create_blog as create_blog_db,
    get_blogs as get_all_blogs_db,
    get_blog as get_single_blog_db,
    edit_blog as edit_blog_db,
    delete_blog as delete_blog_db
)




router = APIRouter(
    tags=['blog']
)

@router.post('/create_blog', response_model=schemas.BlogResponse, status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, background_tasks: BackgroundTasks, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    background_tasks.add_task(send_email,get_current_user.email,"Blog Created Successfully")
    return create_blog_db(request, db)

@router.get('/blogs/', response_model=List[schemas.BlogResponse])
def get_all_blogs(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return get_all_blogs_db(db)

@router.get('/blog/{blog_id}', response_model=schemas.BlogResponse)
def get_single_blog(blog_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return get_single_blog_db(blog_id, db)

@router.put('/edit_blog/{blog_id}', response_model=schemas.BlogResponse, status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id: int, request: schemas.BlogCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return edit_blog_db(blog_id, request, db)

@router.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_blog(blog_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return delete_blog_db(blog_id, db)
