# FastAPI Blog API

A RESTful API for managing blog posts and users built with FastAPI and SQLAlchemy. This API provides JWT authentication and CRUD operations for blogs and users.

## Features

- User management (registration, authentication, profile retrieval)
- Blog post operations (create, read, update, delete)
- JWT-based authentication with Bearer token
- Pydantic models for request/response validation
- SQLAlchemy ORM with SQLite database
- Password hashing using bcrypt

## API Endpoints

### Authentication
- `POST /user/token`
  - Login endpoint to get access token
  - Request body: Form data with username (email) and password
  - Response: `{"access_token": "string", "token_type": "bearer"}`

### User Operations
- `POST /user/create_user`
  - Register new user
  - Request body: 
    ```json
    {
        "user_name": "string",
        "email": "string",
        "password": "string"
    }
    ```
  - Response: User details with associated blogs

- `GET /user/get_user/{user_id}`
  - Get user profile with their blogs
  - Protected: Requires authentication
  - Response: User details including list of blogs

### Blog Operations
- `POST /create_blog`
  - Create a new blog post
  - Protected: Requires authentication
  - Request body:
    ```json
    {
        "title": "string",
        "content": "string",
        "author_id": integer
    }
    ```

- `GET /blogs/`
  - Get all blog posts
  - Protected: Requires authentication
  - Response: Array of blog posts with author details

- `GET /blog/{blog_id}`
  - Get a specific blog post
  - Protected: Requires authentication
  - Response: Blog post with author details

- `PUT /edit_blog/{blog_id}`
  - Update an existing blog post
  - Protected: Requires authentication
  - Request body: Same as create blog

- `DELETE /blog/{blog_id}`
  - Delete a blog post
  - Protected: Requires authentication
  - Response: 204 No Content

## Project Structure

```
├── database.py       # Database configuration & session management
├── hash.py          # Password hashing utilities using bcrypt
├── jwt_token.py     # JWT token generation and verification
├── main.py          # FastAPI application entry point
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic models for request/response
├── oauth2.py        # OAuth2 authentication implementation
├── repository/      # Business logic implementation
│   ├── blog.py     # Blog CRUD operations
│   ├── user.py     # User management operations
│   └── login.py    # Authentication logic
└── routers/        # API route handlers
    ├── blog.py     # Blog endpoints
    ├── user.py     # User endpoints
    └── login.py    # Authentication endpoints
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
pip install fastapi sqlalchemy uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart
```

4. Run the application:
```sh
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Authentication

The API uses JWT Bearer token authentication. To access protected endpoints:

1. Get a token from `/user/token` endpoint using your credentials
2. Include the token in the Authorization header:
   ```
   Authorization: Bearer <your_token>
   ```

## API Documentation

Once running, view the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Database

The API uses SQLite database (blog.db) by default. The database will be automatically created when you first run the application.

## Error Handling

The API implements proper error handling with appropriate HTTP status codes:
- 400: Bad Request
- 401: Unauthorized
- 404: Resource Not Found
- 500: Internal Server Error