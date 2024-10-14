from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException

from app.data import database

from app.errors.exeptions import Missing
from app.service import activity as service
from app.models.activity import Activity, ActivityCreate


router = APIRouter(prefix="/activity")


@router.get("")
@router.get("/")
def get_activies() -> list[Activity]:
    return service.get_all()


@router.get("/{activity_id}")
def get_activity(activity_id: int) -> Activity:
    try:
        return service.get_one(activity_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post("/")
def create_activity(
    activity: ActivityCreate,
    session: AsyncSession = Depends(database.session_dependency),
) -> Activity:
    return service.create(session, activity)


@router.patch("/{activity_id}")
def modify(
    activity_id: int,
    activity: ActivityCreate,
    session: AsyncSession = Depends(database.session_dependency),
) -> Activity:
    try:
        return service.modify(activity_id, activity)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete("/{activity_id}")
def delete(
    activity_id: int,
    session: AsyncSession = Depends(database.session_dependency),
):
    try:
        return service.delete(session, activity_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
