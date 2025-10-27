from enum import Enum as PyEnum

from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Librarian(Base):
    __tablename__ = "librarians"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    contact = Column(String(50), nullable=True)
    librarian_id_image = Column(String(255), nullable=True)