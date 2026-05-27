from fastapi import APIRouter, Depends

from src.app.auth.service import AuthService
from src.app.auth.dependencies import get_auth_service

from src.app.auth.schema import LoginRequest, JWTResponse

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login", response_model=JWTResponse)
def login(
    data: LoginRequest,
    service: AuthService = Depends(get_auth_service)
):
    return service.login(
        email=data.email,
        password=data.password
    )
