from enum import Enum as PyEnum

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class BookStatus(PyEnum):
    AVAILABLE = "available"
    BORROWED = "borrowed"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    isbn = Column(String(64), unique=True, nullable=True)
    category = Column(String(100), nullable=True)
    pages = Column(Integer, nullable=True)
    call_numbers = Column(String(255), nullable=True)
    book_type = Column(String(100), nullable=True)
    book_location = Column(String(100), nullable=True)

    acquisition = relationship(
        "BookAcquisition", back_populates="book", uselist=False, cascade="all, delete-orphan"
    )
    inventory = relationship(
        "BookInventory", back_populates="book", uselist=False, cascade="all, delete-orphan"
    )
    transactions = relationship("Transaction", back_populates="book")
