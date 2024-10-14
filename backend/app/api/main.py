from fastapi import APIRouter
from app.api.routes import activity

api_router = APIRouter()
api_router.include_router(activity.router, tags=["Activity tracker"])
