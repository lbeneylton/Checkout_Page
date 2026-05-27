from src.app.users.repository import UserRepository

from app.core.security.password import verify_password
from app.core.security.jwt import create_access_token


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, email: str, password: str):
        user = self.user_repository.get_active_by_email(email)

        # Verifica se o email está ativo
        if not user:
            raise Exception("Invalid credentials")

        # Verifica se a senha está correta
        if not verify_password(password, user.password_hash):
            raise Exception("Invalid credentials")

        # Cria o token
        token = create_access_token(
            data={
                "sub": str(user.user_id),
                "email": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }
