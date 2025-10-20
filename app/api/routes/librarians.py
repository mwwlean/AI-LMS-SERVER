from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_librarian_service
from app.schemas.librarian import (
    LibrarianCreate,
    LibrarianRead,
    LibrarianUpdate,
)
from app.services.librarian_service import LibrarianService

router = APIRouter(prefix="/librarians", tags=["librarians"])


@router.get("/", response_model=List[LibrarianRead])
def list_librarians(
    service: LibrarianService = Depends(get_librarian_service),
):
    return service.list_librarians()


@router.post(
    "/",
    response_model=LibrarianRead,
    status_code=status.HTTP_201_CREATED,
)
def create_librarian(
    payload: LibrarianCreate,
    service: LibrarianService = Depends(get_librarian_service),
):
    return service.create_librarian(payload)


@router.get("/{librarian_id}", response_model=LibrarianRead)
def get_librarian(
    librarian_id: int,
    service: LibrarianService = Depends(get_librarian_service),
):
    librarian = service.get_librarian(librarian_id)
    if not librarian:
        raise HTTPException(status_code=404, detail="Librarian not found")
    return librarian


@router.put("/{librarian_id}", response_model=LibrarianRead)
def update_librarian(
    librarian_id: int,
    payload: LibrarianUpdate,
    service: LibrarianService = Depends(get_librarian_service),
):
    librarian = service.update_librarian(librarian_id, payload)
    if not librarian:
        raise HTTPException(status_code=404, detail="Librarian not found")
    return librarian


@router.delete(
    "/{librarian_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_librarian(
    librarian_id: int,
    service: LibrarianService = Depends(get_librarian_service),
):
    removed = service.delete_librarian(librarian_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Librarian not found")