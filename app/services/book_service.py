from typing import List, Optional

from sqlalchemy.orm import Session

from app.repositories.book_repository import BookRepository
from app.schemas.book import BookCreate, BookRead, BookUpdate


class BookService:
    """Business logic for book operations."""

    def __init__(self, db: Session):
        self.repository = BookRepository(db)

    def list_books(self) -> List[BookRead]:
        books = self.repository.list()
        return [BookRead.model_validate(book) for book in books]

    def get_book(self, book_id: int) -> Optional[BookRead]:
        book = self.repository.get(book_id)
        if not book:
            return None
        return BookRead.model_validate(book)

    def create_book(self, dto: BookCreate) -> BookRead:
        payload = dto.model_dump(exclude_none=True)
        book = self.repository.create(payload)
        return BookRead.model_validate(book)

    def update_book(
        self,
        book_id: int,
        dto: BookUpdate,
    ) -> Optional[BookRead]:
        book = self.repository.get(book_id)
        if not book:
            return None
        data = dto.model_dump(exclude_unset=True, exclude_none=True)
        updated = self.repository.update(book, data)
        return BookRead.model_validate(updated)

    def delete_book(self, book_id: int) -> bool:
        book = self.repository.get(book_id)
        if not book:
            return False
        self.repository.delete(book)
        return True
