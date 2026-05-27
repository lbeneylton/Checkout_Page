from fastapi import Depends
from src.app.users.repository import UserRepository
from src.app.users.service import UserService
from src.app.core.dependencies import get_session


def get_user_repository(session=Depends(get_session)) -> UserRepository:
    return UserRepository(session)


def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repository)
