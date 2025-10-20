from fastapi import FastAPI

from app.api.routes import api_router
from app.core.config import get_settings
from app.core.database import Base, engine
# Import models to ensure metadata registration
from app.models import book, transaction, user  # noqa: F401


def create_tables() -> None:
	Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
	settings = get_settings()
	application = FastAPI(title=settings.app_name)
	application.include_router(api_router)
	return application


create_tables()
app = create_app()
