from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String[255], nullable=False, index = True)
    description = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=False)
    
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    cover_image = Column(String[255], nullable=True) #Save path, example: static/covers/abc.jpg
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate =func.now(), nullable=False)


    #Relationship with Author, category
    author = relationship('Author', back_populates='books')
    category = relationship('Category', back_populates='books')
    