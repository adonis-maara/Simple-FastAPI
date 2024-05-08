from fastapi import FastAPI
from app.user.routes import router as user_router
from app.auth import router as auth_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])

app.include_router(auth_router, prefix="/auth", tags=["auth"])
