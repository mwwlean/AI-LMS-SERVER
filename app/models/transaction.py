from sqlalchemy import Column, Enum, ForeignKey, Integer, TIMESTAMP

from app.core.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(Enum("borrow", "return", name="transaction_type"), nullable=False)
    status = Column(Enum("pending", "done", name="transaction_status"), default="pending")
    timestamp = Column(TIMESTAMP)
