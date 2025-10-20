from sqlalchemy import Column, Enum, Integer, String, TIMESTAMP

from app.core.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    isbn = Column(String(64), unique=True)
    published_year = Column(Integer)
    copies_available = Column(Integer, default=0)
    category = Column(String(100), nullable=True)
    status = Column(Enum("available", "borrowed", name="book_status"), default="available")
    added_at = Column(TIMESTAMP)
