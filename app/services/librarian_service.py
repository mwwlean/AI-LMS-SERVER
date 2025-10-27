from typing import Optional, Sequence

from sqlalchemy.orm import Session

from app.models.librarian import Librarian
from app.repositories.librarian_repository import LibrarianRepository
from app.schemas.librarian import LibrarianCreate, LibrarianUpdate


class LibrarianService:
    def __init__(self, db: Session):
        self.repository = LibrarianRepository(db)

    def list_librarians(self) -> Sequence[Librarian]:
        return self.repository.list()

    def get_librarian(self, librarian_id: int) -> Optional[Librarian]:
        return self.repository.get(librarian_id)

    def create_librarian(self, dto: LibrarianCreate) -> Librarian:
        data = dto.model_dump()
        return self.repository.create(data)

    def update_librarian(
        self,
        librarian_id: int,
        dto: LibrarianUpdate,
    ) -> Optional[Librarian]:
        librarian = self.repository.get(librarian_id)
        if not librarian:
            return None
        data = dto.model_dump(exclude_unset=True)
        return self.repository.update(librarian, data)

    def delete_librarian(self, librarian_id: int) -> bool:
        librarian = self.repository.get(librarian_id)
        if not librarian:
            return False
        self.repository.delete(librarian)
        return True