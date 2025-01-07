from database import Base
from sqlalchemy import Column, Integer, String,ForeignKey,Table
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blog'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    author_id=Column(Integer,ForeignKey('user.id'))
    author=relationship("User",back_populates='blogs')

class User(Base):
    __tablename__='user'

    id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String)
    email=Column(String,unique=True)
    password=Column(String)
    blogs=relationship("Blog",back_populates='author')


# class User(Base):
#     __tablename__='user'

#     id=Column(Integer,primary_key=True,index=True)
#     user_name=Column(String,index=True)
#     password=Column(String)
#     profile=relationship("Profile",back_populates='user',uselist=False) 
#     posts=relationship("Posts",back_populates='author')

# class Profile(Base):
#     __tablename__='profile'

#     id=Column(Integer,primary_key=True,index=True)
#     first_name=Column(String)
#     last_name=Column(String)
#     user_id=Column(Integer,ForeignKey('user.id'),unique=True)
#     user=relationship("User",back_populates='profile')

# post_tag=Table(
#     "post_tag",
#     Base.metadata,
#     Column("post_id",Integer,ForeignKey("posts.id"),primary_key=True),
#     Column("tag_id",Integer,ForeignKey("tags.id"),primary_key=True)
# )

# class Post(Base): 
#     __tablename__='posts'
#     id=Column(Integer,primary_key=True,index=True)
#     title=Column(String)
#     content=Column(String)
#     author_id=Column(Integer,ForeignKey('user.id'))
#     author=relationship("User",back_populates='posts')
#     tags=relationship("Tag",secondary=post_tag,back_populates="posts")

# class Tag(Base):
#     __tablename__='tags'
#     id=Column(Integer,primary_key=True,index=True)
#     tag_name=Column(String,unique=True)
#     posts=relationship("Post",secondary=post_tag,back_populates="tags")
