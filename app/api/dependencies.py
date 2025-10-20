from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.book_service import BookService
from app.services.librarian_service import LibrarianService
from app.services.user_service import UserService


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


def get_book_service(db: Session = Depends(get_db)) -> BookService:
    return BookService(db)


def get_librarian_service(db: Session = Depends(get_db)) -> LibrarianService:
    return LibrarianService(db)


