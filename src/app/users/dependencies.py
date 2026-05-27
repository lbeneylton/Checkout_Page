from fastapi import Depends
from src.app.users.repository import UserRepository
from src.app.users.service import UserService
from src.app.core.dependencies import get_session


def get_user_service(session=Depends(get_session)) -> UserService:
    repository = UserRepository(session)
    return UserService(repository)
