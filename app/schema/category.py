from pydantic import BaseModel

class CategoryBase(BaseModel): 
    name: str
    description: str | None = None

class CategoryCreate(CategoryBase):
    """Schema for creating a new category"""
    pass

class CategoryUpdate(CategoryBase):
    """Schema for updating an existing category"""
    name: str | None = None
    description: str | None = None
    
class CategoryInDBBase(CategoryBase):
    id: int

    class Config:
        orm_mode = True #Pydantic read from SQLAlchemy model

class Category(CategoryInDBBase):
    """Schema for returning category data to client"""
    pass