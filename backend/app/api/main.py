from fastapi import APIRouter
from app.api.routes import time_tracker, user

api_router = APIRouter()
api_router.include_router(user.router, tags=["User"])
api_router.include_router(time_tracker.router, tags=["Time tracker"])
