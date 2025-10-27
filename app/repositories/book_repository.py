from typing import List, Optional

from sqlalchemy.orm import Session, selectinload

from app.models.book import Book
from app.models.book_acquisition import BookAcquisition
from app.models.book_call_number import BookCallNumber
from app.models.book_inventory import BookInventory


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> List[Book]:
        return (
            self.db.query(Book)
            .options(
                selectinload(Book.type),
                selectinload(Book.location),
                selectinload(Book.acquisition),
                selectinload(Book.call_number),
                selectinload(Book.inventory),
            )
            .all()
        )

    def get(self, book_id: int) -> Optional[Book]:
        return (
            self.db.query(Book)
            .options(
                selectinload(Book.type),
                selectinload(Book.location),
                selectinload(Book.acquisition),
                selectinload(Book.call_number),
                selectinload(Book.inventory),
            )
            .filter(Book.id == book_id)
            .first()
        )

    def create(self, data: dict) -> Book:
        acquisition_data = data.pop("acquisition", None)
        call_number_data = data.pop("call_number", None)
        inventory_data = data.pop("inventory", None)

        book = Book(**data)

        if acquisition_data:
            book.acquisition = BookAcquisition(**acquisition_data)
        if call_number_data:
            book.call_number = BookCallNumber(**call_number_data)
        if inventory_data:
            book.inventory = BookInventory(**inventory_data)

        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, book: Book, data: dict) -> Book:
        acquisition_data = data.pop("acquisition", None)
        call_number_data = data.pop("call_number", None)
        inventory_data = data.pop("inventory", None)

        for key, value in data.items():
            setattr(book, key, value)

        if acquisition_data is not None:
            if book.acquisition:
                for key, value in acquisition_data.items():
                    setattr(book.acquisition, key, value)
            elif acquisition_data:
                book.acquisition = BookAcquisition(**acquisition_data)

        if call_number_data is not None:
            if book.call_number:
                for key, value in call_number_data.items():
                    setattr(book.call_number, key, value)
            elif call_number_data:
                book.call_number = BookCallNumber(**call_number_data)

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
