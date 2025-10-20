from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserRead, UserUpdate
from passlib.context import CryptContext
from typing import List, Optional
from sqlalchemy.orm import Session


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    """Business logic for user operations."""

    def __init__(self, db: Session) -> None:
        self.repository = UserRepository(db)

    def list_users(self) -> List[UserRead]:
        users = self.repository.list()
        return [UserRead.model_validate(user) for user in users]

    def get_user(self, user_id: int) -> Optional[UserRead]:
        user = self.repository.get(user_id)
        if not user:
            return None
        return UserRead.model_validate(user)

    def create_user(self, data: UserCreate) -> UserRead:
        payload = data.model_dump()
        payload["password"] = pwd_context.hash(payload["password"])
        user = self.repository.create(payload)
        return UserRead.model_validate(user)

    def update_user(self, user_id: int, data: UserUpdate) -> Optional[UserRead]:
        changes = {
            key: value
            for key, value in data.model_dump(exclude_unset=True).items()
        }
        if "password" in changes and changes["password"]:
            changes["password"] = pwd_context.hash(changes["password"])
        user = self.repository.update(user_id, changes)
        return UserRead.model_validate(user) if user else None

    def delete_user(self, user_id: int) -> bool:
        user = self.repository.get(user_id)
        if not user:
            return False
        self.repository.delete(user)
        return True
