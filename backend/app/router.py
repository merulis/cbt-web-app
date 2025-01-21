from fastapi import APIRouter
from app.apps.activity import routes as activity
from app.apps.auth.routers import routes as user
from app.apps.auth.routers import routes as auth

api_router = APIRouter()
api_router.include_router(user.router, tags=["User"])
api_router.include_router(auth.router, tags=["Auth"])
api_router.include_router(activity.router, tags=["Activity"])
