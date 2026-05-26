from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=64
    )


class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
