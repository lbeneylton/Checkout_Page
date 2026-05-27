from sqlalchemy.orm import Session
from sqlalchemy import select, update
from src.app.users.models import User

from src.app.core.logger import logging

from datetime import datetime, UTC

logger = logging.getLogger(__name__)


class UserRepository:
    def __init__(self, session: Session) -> None:
        logger.debug("Repositorio de usuario criado")
        self.session = session

    def create(self, user: User) -> User:
        self.session.add(user)
        return user

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.execute(
            select(User).where(
                User.user_id == user_id,
                User.deleted_at.is_(None)
            )
        ).scalar_one_or_none()

    def get_by_email(self, email: str) -> User | None:
        return self.session.execute(
            select(User).where(
                User.email == email,
                User.deleted_at.is_(None)
            )
        ).scalar_one_or_none()

    def delete(self, user_id: int):  # sem commit
        user = self.get_by_id(user_id)

        if not user:
            return None

        user.deleted_at = datetime.now(UTC)
        return user
