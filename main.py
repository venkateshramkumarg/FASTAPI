from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import blog, user,login
import time

app = FastAPI()

# Create database tables
Base.metadata.create_all(engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.middleware("http")
async def log_requests(request:Request,call_next):
    start_time=time.time()

    print(f"Request: {request.method} {request.url}")

    response=await call_next(request)

    process_time=time.time()-start_time

    print(f"Response : {response.status_code}, Time: {process_time:.2f}s")

    return response

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)

@app.get('/')
def index():
    return "Hello"





