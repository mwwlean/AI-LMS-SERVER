from typing import Optional, Sequence

from sqlalchemy.orm import Session

from app.models.librarian import Librarian


class LibrarianRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> Sequence[Librarian]:
        return self.db.query(Librarian).all()

    def get(self, librarian_id: int) -> Optional[Librarian]:
        return (
            self.db.query(Librarian)
            .filter(Librarian.id == librarian_id)
            .first()
        )

    def create(self, data: dict) -> Librarian:
        librarian = Librarian(**data)
        self.db.add(librarian)
        self.db.commit()
        self.db.refresh(librarian)
        return librarian

    def update(self, librarian: Librarian, data: dict) -> Librarian:
        for key, value in data.items():
            setattr(librarian, key, value)
        self.db.commit()
        self.db.refresh(librarian)
        return librarian

    def delete(self, librarian: Librarian) -> None:
        self.db.delete(librarian)
        self.db.commit()