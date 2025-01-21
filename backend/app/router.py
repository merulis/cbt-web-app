from fastapi import APIRouter
from app.apps.activity import routes as activity_routes
from app.apps.auth import routes as auth_routes
from app.apps.activity import routes as user_routes


api_router = APIRouter()

api_router.include_router(user_routes.router, tags=["User"])
api_router.include_router(auth_routes.router, tags=["Auth"])
api_router.include_router(activity_routes.router, tags=["Activity"])
