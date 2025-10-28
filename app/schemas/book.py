from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.book import BookStatus


class BookAcquisitionBase(BaseModel):
    date_received: Optional[date] = None
    source_of_fund: Optional[str] = None
    place: Optional[str] = None
    publisher: Optional[str] = None
    published_year: Optional[int] = None
    date_copyright: Optional[date] = None


class BookAcquisitionCreate(BookAcquisitionBase):
    pass


class BookAcquisitionRead(BookAcquisitionBase):
    class Config:
        from_attributes = True


class BookInventoryBase(BaseModel):
    total_copies: Optional[int] = None
    copies_available: Optional[int] = None
    status: Optional[BookStatus] = BookStatus.AVAILABLE
    added_at: Optional[datetime] = None

    model_config = ConfigDict(use_enum_values=True)


class BookInventoryCreate(BookInventoryBase):
    pass


class BookInventoryRead(BookInventoryBase):
    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    category: Optional[str] = None
    call_numbers: Optional[str] = None
    book_type: Optional[str] = None
    book_location: Optional[str] = None


class BookCreate(BookBase):
    acquisition: Optional[BookAcquisitionCreate] = None
    inventory: Optional[BookInventoryCreate] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    category: Optional[str] = None
    call_numbers: Optional[str] = None
    book_type: Optional[str] = None
    book_location: Optional[str] = None
    acquisition: Optional[BookAcquisitionCreate] = None
    inventory: Optional[BookInventoryCreate] = None


class BookRead(BookBase):
    id: int
    acquisition: Optional[BookAcquisitionRead] = None
    inventory: Optional[BookInventoryRead] = None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
