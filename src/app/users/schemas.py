from pydantic import BaseModel, EmailStr, Field
from src.app.users.enums import RoleType


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=64
    )
    role: RoleType = RoleType.client


class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
