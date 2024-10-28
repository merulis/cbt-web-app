from fastapi import APIRouter
from app.api import activity
from app.api import user
from app.api import auth

api_router = APIRouter()
api_router.include_router(user.router, tags=["User"])
api_router.include_router(auth.router, tags=["Auth"])
api_router.include_router(activity.router, tags=["Activity"])
