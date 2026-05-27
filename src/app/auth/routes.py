from fastapi import APIRouter, Depends

from src.app.auth.service import AuthService
from src.app.users.repository import UserRepository
from src.app.core.dependencies import get_session

from src.app.auth.schema import LoginRequest

auth_router = APIRouter()


@auth_router.post("/login")
def login(
    data: LoginRequest,
    session=Depends(get_session)
):
    repo = UserRepository(session)
    auth_service = AuthService(repo)

    result = auth_service.login(
        email=data.email,
        password=data.password
    )

    return result
