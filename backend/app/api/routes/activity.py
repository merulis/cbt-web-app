from fastapi import APIRouter, HTTPException
from app.errors.exeptions import Missing
from app.models.activity import Activity, ActivityBase
from app.service import activity as service


router = APIRouter(prefix="/activity")


@router.get("")
@router.get("/")
def get_all() -> list[Activity]:
    return service.get_all()


@router.get("/{id}")
def get_one(id) -> Activity:
    try:
        return service.get_one(id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post("/")
def create(activity: ActivityBase) -> Activity:
    return service.create(activity)


@router.patch("/{id}")
def modify(id: int, activity: ActivityBase) -> Activity:
    try:
        return service.modify(id, activity)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.put("/{id}")
def replace(id: int, activity: ActivityBase) -> Activity:
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
