# FastAPI Blog API

A RESTful API for managing blog posts and users built with FastAPI and SQLAlchemy.

## Features

- User management (create, get user details)
- Blog post operations (create, read, update, delete)
- JWT-based authentication
- Pydantic models for request/response validation
- SQLAlchemy ORM for database operations

## API Endpoints

### Blog Operations
- `POST /create_blog` - Create a new blog post
- `GET /blogs/` - Get all blog posts
- `GET /blog/{blog_id}` - Get a specific blog post
- `PUT /edit_blog/{blog_id}` - Update a blog post
- `DELETE /blog/{blog_id}` - Delete a blog post

### User Operations
- User registration and authentication endpoints
- Get user details with associated blogs

## Project Structure

```
├── database.py       # Database configuration
├── hash.py          # Password hashing utilities
├── jwt_token.py     # JWT token handling
├── main.py          # FastAPI application entry point
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic models
├── repository/      # Repository pattern implementation
│   ├── blog.py     # Blog CRUD operations
│   └── user.py     # User operations
└── routers/        # API route handlers
    ├── blog.py     # Blog endpoints
    └── user.py     # User endpoints
```

## Setup and Installation

1. Create a virtual environment:
```sh
python -m venv env
```

2. Activate the virtual environment:
```sh
# Windows
env\Scripts\activate
# Unix/MacOS
source env/bin/activate
```

3. Install dependencies:
```sh
pip install fastapi sqlalchemy uvicorn python-jose[cryptography] passlib[bcrypt]
```

4. Run the application:
```sh
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, view the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`