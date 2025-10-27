from typing import Optional

from pydantic import BaseModel, EmailStr


class LibrarianBase(BaseModel):
    name: str
    email: EmailStr
    contact: Optional[str] = None
    librarian_id_image: Optional[str] = None


class LibrarianCreate(LibrarianBase):
    pass


class LibrarianUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    contact: Optional[str] = None
    librarian_id_image: Optional[str] = None


class LibrarianRead(LibrarianBase):
    id: int

    class Config:
        from_attributes = True