from fastapi import HTTPException,status
from sqlalchemy.orm import Session
import schemas,models

def create_blog(request:schemas.BlogCreate,db:Session):
 
    new_blog = models.Blog(title=request.title, content=request.content, author_id=request.author_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blogs(db:Session):

    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No blogs found")
    return blogs     

def get_blog(blog_id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    return blog   

def edit_blog(blog_id:int,request:schemas.BlogCreate,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f'Blog with id {blog_id} not found')

    blog.title=request.title
    blog.content=request.content
    db.commit()
    db.refresh(blog)
    return blog

def delete_blog(blog_id:int,db:Session):
    blog_query=db.query(models.Blog).filter(models.Blog.id==blog_id)
    blog=blog_query.first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {blog_id} not found')

    blog_query.delete(synchronize_session=False)
    db.commit()
    return {"message":"Item deleted"}