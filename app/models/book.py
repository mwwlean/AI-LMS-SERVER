from enum import Enum as PyEnum

from sqlalchemy import (
    Column,
    Date,
    Enum,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class BookStatus(PyEnum):
    AVAILABLE = "available"
    BORROWED = "borrowed"


class BookType(Base):
    __tablename__ = "book_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    books = relationship("Book", back_populates="type")


class BookLocation(Base):
    __tablename__ = "book_locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    books = relationship("Book", back_populates="location")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    isbn = Column(String(64), unique=True, nullable=True)
    category = Column(String(100), nullable=True)
    type_id = Column(Integer, ForeignKey("book_types.id"), nullable=True)
    location_id = Column(Integer, ForeignKey("book_locations.id"), nullable=True)

    type = relationship("BookType", back_populates="books")
    location = relationship("BookLocation", back_populates="books")
    acquisition = relationship(
        "BookAcquisition", back_populates="book", uselist=False, cascade="all, delete-orphan"
    )
    call_number = relationship(
        "BookCallNumber", back_populates="book", uselist=False, cascade="all, delete-orphan"
    )
    inventory = relationship(
        "BookInventory", back_populates="book", uselist=False, cascade="all, delete-orphan"
    )
    transactions = relationship("Transaction", back_populates="book")
