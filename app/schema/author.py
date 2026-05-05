from pydantic import BaseModel

class AuthorBase(BaseModel): 
    name: str
    bio: str | None = None

class AuthorCreate(AuthorBase):
    """Schema for creating a new author"""
    pass

class AuthorUpdate(AuthorBase):
    """Schema for updating an existing author"""
    name: str | None = None
    bio: str | None = None

class AuthorInDBBase(AuthorBase):
    id: int

    class Config:
        orm_mode = True #Pydantic read from SQLAlchemy model

class Author(AuthorInDBBase):
    """Schema for returning author data to client"""
    pass