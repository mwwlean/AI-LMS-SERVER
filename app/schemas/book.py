from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, field_validator
from pydantic import ConfigDict

from app.models.book import BookStatus


class BookCallNumberBase(BaseModel):
    classification: Optional[str] = None
    copyright: Optional[str] = None
    authors: Optional[str] = None
    copy: Optional[str] = None


class BookCallNumberCreate(BookCallNumberBase):
    pass


class BookCallNumberRead(BookCallNumberBase):
    class Config:
        from_attributes = True


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


class BookTypeRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class BookLocationRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    category: Optional[str] = None
    type_id: Optional[int] = None
    location_id: Optional[int] = None

    @field_validator("type_id", "location_id", mode="before")
    def _normalize_fk(cls, value):
        if value in (None, ""):
            return None
        try:
            ivalue = int(value)
        except (TypeError, ValueError):
            return value
        return ivalue if ivalue > 0 else None


class BookCreate(BookBase):
    acquisition: Optional[BookAcquisitionCreate] = None
    call_number: Optional[BookCallNumberCreate] = None
    inventory: Optional[BookInventoryCreate] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    category: Optional[str] = None
    type_id: Optional[int] = None
    location_id: Optional[int] = None
    acquisition: Optional[BookAcquisitionCreate] = None
    call_number: Optional[BookCallNumberCreate] = None
    inventory: Optional[BookInventoryCreate] = None

    @field_validator("type_id", "location_id", mode="before")
    def _normalize_fk(cls, value):
        if value in (None, ""):
            return None
        try:
            ivalue = int(value)
        except (TypeError, ValueError):
            return value
        return ivalue if ivalue > 0 else None


class BookRead(BookBase):
    id: int
    type: Optional[BookTypeRead] = None
    location: Optional[BookLocationRead] = None
    acquisition: Optional[BookAcquisitionRead] = None
    call_number: Optional[BookCallNumberRead] = None
    inventory: Optional[BookInventoryRead] = None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
