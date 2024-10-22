from fastapi import APIRouter
from app.api import activity
from app.api import user
from app.api import login

api_router = APIRouter()
api_router.include_router(user.router, tags=["User"])
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(activity.router, tags=["Activity"])
