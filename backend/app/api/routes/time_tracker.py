from fastapi import APIRouter, HTTPException
from app.errors.db import Missing
from app.models.activity import ActivityRecord, NewActivityRecord
from app.service import time_tracker as service


router = APIRouter(prefix="/activity")


@router.get("")
@router.get("/")
def get_all() -> list[ActivityRecord]:
    return service.get_all()


@router.get("/{id}")
def get_one(id) -> ActivityRecord:
    try:
        return service.get_one(id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post("/")
def create(activity: NewActivityRecord) -> NewActivityRecord:
    return service.create(activity)


@router.patch("/{id}")
def modify(id: int, activity: ActivityRecord) -> ActivityRecord:
    try:
        return service.modify(id, activity)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.put("/{id}")
def replace(id: int, activity: ActivityRecord) -> ActivityRecord:
    try:
        return service.replace(id, activity)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete("/{id}")
def delete(id: int):
    try:
        return service.delete(id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
