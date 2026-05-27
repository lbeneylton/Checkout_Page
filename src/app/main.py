from app.auth.dependencies import get_current_user
from fastapi import Depends
from fastapi import FastAPI

from src.app.users.routes import user_router
from src.app.auth.routes import auth_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)


@app.get("/protected")
def protected_route(user=Depends(get_current_user)):
    return {
        "message": "OK",
        "user": user["sub"]
    }
