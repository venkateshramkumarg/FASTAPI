from fastapi import FastAPI
from database import engine, Base
from routers import blog, user,login

app = FastAPI()

# Create database tables
Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)

@app.get('/')
def index():
    return "Hello"





