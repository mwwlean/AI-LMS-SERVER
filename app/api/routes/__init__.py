from fastapi import APIRouter

from app.api.routes import books, librarians, users

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(books.router)
api_router.include_router(librarians.router)

__all__ = ["api_router"]
