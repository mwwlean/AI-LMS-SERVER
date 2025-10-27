from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class BookCallNumber(Base):
    __tablename__ = "book_call_numbers"

    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    classification = Column(String(50), nullable=True)
    copyright = Column(String(50), nullable=True)
    authors = Column(String(50), nullable=True)
    copy = Column(String(50), nullable=True)

    book = relationship("Book", back_populates="call_number")