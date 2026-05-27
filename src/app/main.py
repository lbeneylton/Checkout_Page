from fastapi import FastAPI

from src.app.users.routes import router

app = FastAPI()

app.include_router(router)
