from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_book_service
from app.schemas.book import BookCreate, BookRead, BookUpdate
from app.services.book_service import BookService

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=List[BookRead])
def list_books(service: BookService = Depends(get_book_service)):
    return service.list_books()


@router.post(
    "/",
    response_model=BookRead,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    payload: BookCreate,
    service: BookService = Depends(get_book_service),
):
    return service.create_book(payload)


@router.get("/{book_id}", response_model=BookRead)
def get_book(
    book_id: int,
    service: BookService = Depends(get_book_service),
):
    result = service.get_book(book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return result


@router.put("/{book_id}", response_model=BookRead)
def update_book(
    book_id: int,
    payload: BookUpdate,
    service: BookService = Depends(get_book_service),
):
    result = service.update_book(book_id, payload)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return result


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    service: BookService = Depends(get_book_service),
):
    removed = service.delete_book(book_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Book not found")
