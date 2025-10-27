from sqlalchemy import Column, Enum, ForeignKey, Integer, TIMESTAMP
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.book import BookStatus


class BookInventory(Base):
    __tablename__ = "book_inventory"

    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    total_copies = Column(Integer, nullable=False, default=0)
    copies_available = Column(Integer, nullable=False, default=0)
    status = Column(
        Enum(
            BookStatus,
            values_callable=lambda enum_cls: [member.value for member in enum_cls],
            native_enum=False,
            name="book_status",
        ),
        nullable=False,
        default=BookStatus.AVAILABLE.value,
    )
    added_at = Column(TIMESTAMP, nullable=True)

    book = relationship("Book", back_populates="inventory")