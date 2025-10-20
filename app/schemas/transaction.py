from datetime import datetime

from pydantic import BaseModel


class TransactionResponse(BaseModel):
    id: int
    book_id: int
    user_id: int
    type: str
    status: str
    timestamp: datetime | None = None

    class Config:
        from_attributes = True
