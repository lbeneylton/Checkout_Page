from fastapi import APIRouter, Depends
from src.app.users.dependencies import get_user_service
from src.app.users.schemas import UserCreate, UserResponse
from src.app.users.service import UserService

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return service.create_user(data)
