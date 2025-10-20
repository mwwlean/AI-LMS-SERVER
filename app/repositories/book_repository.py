from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.book import Book


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> List[Book]:
        return self.db.query(Book).all()

    def get(self, book_id: int) -> Optional[Book]:
        return (
            self.db.query(Book)
            .filter(Book.id == book_id)
            .first()
        )

    def create(self, data: dict) -> Book:
        book = Book(**data)
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, book: Book, data: dict) -> Book:
        for key, value in data.items():
            setattr(book, key, value)
        self.db.commit()
        self.db.refresh(book)
        return book

    def delete(self, book: Book) -> None:
        self.db.delete(book)
        self.db.commit()
