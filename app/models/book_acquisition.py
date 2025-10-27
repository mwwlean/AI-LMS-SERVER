from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class BookAcquisition(Base):
    __tablename__ = "book_acquisitions"

    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    date_received = Column(Date, nullable=True)
    source_of_fund = Column(String(255), nullable=True)
    place = Column(String(255), nullable=True)
    publisher = Column(String(255), nullable=True)
    published_year = Column(Integer, nullable=True)
    date_copyright = Column(Date, nullable=True)

    book = relationship("Book", back_populates="acquisition")