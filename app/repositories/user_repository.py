from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """Data access layer for user entities."""

    def __init__(self, db: Session):
        self.session = db

    def list(self) -> List[User]:
        return self.session.query(User).all()

    def get(self, user_id: int) -> Optional[User]:
        return (
            self.session.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def create(self, data: dict) -> User:
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update(self, user_id: int, data: dict) -> Optional[User]:
        user = self.get(user_id)
        if not user:
            return None

        for key, value in data.items():
            setattr(user, key, value)

        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()
