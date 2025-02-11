from fastapi import APIRouter
from app.presentation.routes.user_endpoints import router as user_routes


api_router = APIRouter()

api_router.include_router(user_routes, tags=["User"])
