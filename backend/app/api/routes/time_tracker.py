from fastapi import APIRouter
from app.models.time_tracker import ActivityRecord
from app.service import time_tracker as service


router = APIRouter(prefix="/activity")


@router.get("/")
def get_all() -> list[ActivityRecord]:
    return service.get_all()


@router.get("/{id}")
def get_one(id) -> ActivityRecord:
    return service.get_one(id)


@router.post("/")
def create(activity: ActivityRecord) -> ActivityRecord:
    return service.create(activity)


@router.patch("/{id}")
def modify(id: int, activity: ActivityRecord) -> ActivityRecord:
    return service.modify(id, activity)


@router.put("/{id}")
def replace(id: int, activity: ActivityRecord) -> ActivityRecord:
    return service.replace(id, activity)


@router.delete("/{id}")
def delete(id: int):
    return service.delete(id)
