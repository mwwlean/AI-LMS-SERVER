from typing import Optional

from pydantic import BaseModel, EmailStr


class LibrarianBase(BaseModel):
    full_name: str
    email: EmailStr


class LibrarianCreate(LibrarianBase):
    password: str


class LibrarianUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class LibrarianRead(LibrarianBase):
    id: int

    class Config:
        from_attributes = True