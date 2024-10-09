from fastapi import APIRouter
from app.api.routes import root, time_tracker

api_router = APIRouter()
api_router.include_router(root.router, tags=["root"])
api_router.include_router(time_tracker.router, tags=["Time tracker"])
