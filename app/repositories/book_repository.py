import re
from difflib import SequenceMatcher
from typing import List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session, selectinload

from app.models.book import Book
from app.models.book_acquisition import BookAcquisition
from app.models.book_inventory import BookInventory


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> List[Book]:
        return (
            self.db.query(Book)
            .options(
                selectinload(Book.acquisition),
                selectinload(Book.inventory),
            )
            .all()
        )

    def get(self, book_id: int) -> Optional[Book]:
        return (
            self.db.query(Book)
            .options(
                selectinload(Book.acquisition),
                selectinload(Book.inventory),
            )
            .filter(Book.id == book_id)
            .first()
        )

    def create(self, data: dict) -> Book:
        acquisition_data = data.pop("acquisition", None)
        inventory_data = data.pop("inventory", None)

        book = Book(**data)

        if acquisition_data:
            book.acquisition = BookAcquisition(**acquisition_data)
        if inventory_data:
            book.inventory = BookInventory(**inventory_data)

        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, book: Book, data: dict) -> Book:
        acquisition_data = data.pop("acquisition", None)
        inventory_data = data.pop("inventory", None)

        for key, value in data.items():
            setattr(book, key, value)

        if acquisition_data is not None:
            if book.acquisition:
                for key, value in acquisition_data.items():
                    setattr(book.acquisition, key, value)
            elif acquisition_data:
                book.acquisition = BookAcquisition(**acquisition_data)

        if inventory_data is not None:
            if book.inventory:
                for key, value in inventory_data.items():
                    setattr(book.inventory, key, value)
            elif inventory_data:
                book.inventory = BookInventory(**inventory_data)

        self.db.commit()
        self.db.refresh(book)
        return book

    def delete(self, book: Book) -> None:
        self.db.delete(book)
        self.db.commit()

    def search(self, query: str, limit: int = 5) -> List[Book]:
        terms = [term for term in query.split() if term]
        if not terms:
            return []

        clauses = []
        for term in terms:
            pattern = f"%{term}%"
            clauses.extend(
                [
                    Book.title.ilike(pattern),
                    Book.author.ilike(pattern),
                    Book.category.ilike(pattern),
                    Book.book_type.ilike(pattern),
                    Book.book_location.ilike(pattern),
                    Book.call_numbers.ilike(pattern),
                ]
            )

        results = (
            self.db.query(Book)
            .options(
                selectinload(Book.acquisition),
                selectinload(Book.inventory),
            )
            .filter(or_(*clauses))
            .limit(limit)
            .all()
        )

        if results:
            return results

        candidates = (
            self.db.query(Book)
            .options(
                selectinload(Book.acquisition),
                selectinload(Book.inventory),
            )
            .limit(100)
            .all()
        )

        scored = []
        lowered_query = query.lower()
        for book in candidates:
            ratio = SequenceMatcher(None, book.title.lower(), lowered_query).ratio()
            if ratio >= 0.6:
                scored.append((ratio, book))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [book for _, book in scored[:limit]]
