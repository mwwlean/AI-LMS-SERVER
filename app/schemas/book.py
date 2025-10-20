from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    category: Optional[str] = None
    copies_available: Optional[int] = None


class BookCreate(BookBase):
    title: str
    author: str
    category: Optional[str] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    category: Optional[str] = None
    copies_available: Optional[int] = None


class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True
