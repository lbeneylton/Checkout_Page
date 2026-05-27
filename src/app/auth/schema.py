from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class JWTResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
