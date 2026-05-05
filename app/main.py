from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import authors, books, categories

app = FastAPI(
    title = 'Book management API',
    description = 'A simple API for managing books, authors, and categories.',
    version = '1.0.0'
)

#Include API routers
app.include_router(authors.router, prefix='/authors', tags=['Authors'])
app.include_router(books.router, prefix='/books', tags=['Books'])
app.include_router(categories.router, prefix='/categories', tags=['Categories'])

#Static files for cover images


@app.get('/') 
def read_root():
    return {'message': 'Book management API is running!'}

