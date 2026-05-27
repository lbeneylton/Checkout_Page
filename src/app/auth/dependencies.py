from src.app.auth.service import AuthService
from fastapi import Depends
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

from app.core.security.jwt import decode_token

from src.app.users.repository import UserRepository
from src.app.users.models import User

from src.app.core.dependencies import get_session


security = HTTPBearer()


def get_auth_service(session=Depends(get_session)) -> AuthService:
    return AuthService(UserRepository(session))


# Ajustar depois desacoplar, usar dependei do user
def get_current_user(
    credentials=Depends(security),
    session=Depends(get_session)
) -> User:
    token = credentials.credentials

    payload = decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )

    repo = UserRepository(session)
    user = repo.get_active_by_id(int(user_id))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user
