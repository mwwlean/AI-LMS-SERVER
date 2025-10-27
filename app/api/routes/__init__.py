from fastapi import APIRouter

from app.api.routes import assistant, books, librarians, users

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(librarians.router)
api_router.include_router(books.router)
api_router.include_router(assistant.router)

__all__ = ["api_router"]
