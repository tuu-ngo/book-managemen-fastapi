# FastAPI Book Management System

## Description

This is a REST API built with FastAPI for managing a book library. It allows users to perform CRUD operations on books, authors, and categories. The application uses SQLAlchemy for database interactions, Alembic for database migrations, and supports file uploads for book cover images.

The API is designed to be simple yet powerful, with features like pagination, filtering, and search functionality.

## Features

- **Authors Management**: Create, read, update, and delete authors with unique name validation.
- **Books Management**: Full CRUD for books, including filtering by author, category, publication year, and keyword search in title/description. Supports cover image uploads.
- **Categories Management**: CRUD operations for book categories.
- **Database**: Uses SQLAlchemy ORM with SQLite (configurable) and Alembic for migrations.
- **Static Files**: Serves book cover images via static file mounting.
- **Pagination**: Supports skip/limit pagination for listing endpoints.
- **Validation**: Pydantic schemas for request/response validation.

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "FastAPI - Book manage"
   ```

2. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn sqlalchemy alembic pydantic python-multipart
   ```
   Note: If you have a `requirements.txt` file, you can use `pip install -r requirements.txt` instead.

3. **Set up the database**:
   - The default database is SQLite (`app.db` in the root directory).
   - To change the database, edit `app/core/config.py` and update `SQLALCHEMY_DATABASE_URI`.
   - Run database migrations:
     ```bash
     alembic upgrade head
     ```

4. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

## API Endpoints

### Authors

- `GET /authors/` - List all authors (with pagination: `skip`, `limit`)
- `GET /authors/{author_id}` - Get a specific author by ID
- `POST /authors/` - Create a new author (requires `name` and optional `bio`)
- `PUT /authors/{author_id}` - Update an author (partial update)
- `DELETE /authors/{author_id}` - Delete an author

### Books

- `GET /books/` - List all books (with filters: `author_id`, `category_id`, `year`, `keyword`, and pagination)
- `GET /books/{book_id}` - Get a specific book by ID
- `POST /books/` - Create a new book (supports cover image upload via `cover` field)
- `PUT /books/{book_id}` - Update a book
- `DELETE /books/{book_id}` - Delete a book

### Categories

- `GET /categories/` - List all categories (with pagination)
- `GET /categories/{category_id}` - Get a specific category by ID
- `POST /categories/` - Create a new category
- `PUT /categories/{category_id}` - Update a category
- `DELETE /categories/{category_id}` - Delete a category

### Static Files

- `GET /static/covers/{filename}` - Access uploaded cover images

## Usage

### Running the Server

After installation, start the server with:
```bash
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive API documentation provided by FastAPI/Swagger.

### Example Requests

- **Get all authors**:
  ```bash
  curl -X GET "http://localhost:8000/authors/"
  ```

- **Create an author**:
  ```bash
  curl -X POST "http://localhost:8000/authors/" \
       -H "Content-Type: application/json" \
       -d '{"name": "J.K. Rowling", "bio": "British author"}'
  ```

- **Get books with filters**:
  ```bash
  curl -X GET "http://localhost:8000/books/?author_id=1&keyword=harry"
  ```

- **Upload a book with cover**:
  Use a tool like Postman or curl with multipart/form-data.

### Database Models

- **Author**: id, name (unique), bio
- **Book**: id, title, description, published_year, author_id (foreign key), category_id (foreign key), cover_path
- **Category**: id, name (unique), description

## Project Structure

```
app/
├── api/
│   ├── deps.py          # Database dependency
│   └── endpoints/       # API route handlers
│       ├── authors.py
│       ├── books.py
│       └── categories.py
├── core/
│   └── config.py        # Application settings
├── db/
│   ├── base.py          # Database base configuration
│   └── session.py       # Database session management
├── models/              # SQLAlchemy models
├── schema/              # Pydantic schemas
└── static/covers/       # Uploaded cover images
migrations/              # Alembic migrations
alembic.ini              # Alembic configuration
```

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run tests (if any).
5. Submit a pull request.

## License

This project is licensed under the MIT License.