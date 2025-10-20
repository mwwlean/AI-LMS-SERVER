from typing import Optional, Sequence

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.librarian import Librarian
from app.repositories.librarian_repository import LibrarianRepository
from app.schemas.librarian import LibrarianCreate, LibrarianUpdate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class LibrarianService:
    def __init__(self, db: Session):
        self.repository = LibrarianRepository(db)

    def list_librarians(self) -> Sequence[Librarian]:
        return self.repository.list()

    def get_librarian(self, librarian_id: int) -> Optional[Librarian]:
        return self.repository.get(librarian_id)

    def create_librarian(self, dto: LibrarianCreate) -> Librarian:
        data = dto.model_dump()
        data["password"] = pwd_context.hash(data["password"])
        return self.repository.create(data)

    def update_librarian(
        self,
        librarian_id: int,
        dto: LibrarianUpdate,
    ) -> Optional[Librarian]:
        librarian = self.repository.get(librarian_id)
        if not librarian:
            return None
        data = {
            key: value
            for key, value in dto.model_dump(exclude_unset=True).items()
        }
        if "password" in data and data["password"]:
            data["password"] = pwd_context.hash(data["password"])
        return self.repository.update(librarian, data)

    def delete_librarian(self, librarian_id: int) -> bool:
        librarian = self.repository.get(librarian_id)
        if not librarian:
            return False
        self.repository.delete(librarian)
        return True