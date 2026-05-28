from src.app.users.repository import UserRepository
from src.app.users.models import User

from src.app.core.exceptions import ConflictError

from app.core.security.password import hash_password


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def _ensure_email_available(self, email: str) -> None:
        if self.repository.get_active_by_email(email):
            raise ConflictError("Email já está em uso")

    def create_user(self, data) -> User:
        # 1. regra de negócio
        self._ensure_email_available(data.email)

        # 2. transformação dados -> User
        user = User(
            email=data.email,
            password_hash=hash_password(data.password)
        )

        # 3. persistência
        created_user = self.repository.create(user)

        # 4. commit (por enquanto aqui, depois usar uma unit of work)
        self.repository.session.commit()
        self.repository.session.refresh(user)

        return created_user
