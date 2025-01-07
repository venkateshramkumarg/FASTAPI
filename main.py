from fastapi import FastAPI
from database import engine, Base
from routers import blog, user

app = FastAPI()

# Create database tables
Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)

@app.get('/')
def index():
    return "Hello"





