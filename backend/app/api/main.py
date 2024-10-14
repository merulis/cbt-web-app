from fastapi import APIRouter
from app.api.routes import activity, user

api_router = APIRouter()
api_router.include_router(user.router, tags=["User"])
api_router.include_router(activity.router, tags=["Activity tracker"])
