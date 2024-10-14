from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException

from app.data import database

from app.exeptions.data import Missing
from app.service import activity as service
from app.schemas.activity import Activity, ActivityCreate


router = APIRouter(prefix="/activity")


@router.get("/")
async def get_activies(
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> list[Activity]:
    return await service.get_all(session)


@router.get("/{activity_id}")
async def get_activity(
    activity_id: int,
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> Activity:
    try:
        return await service.get_one(session, activity_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post("/")
async def create_activity(
    activity: ActivityCreate,
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> Activity:
    return await service.create(session, activity)


@router.patch("/{activity_id}")
async def modify_activity(
    activity_id: int,
    activity: ActivityCreate,
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> Activity:
    try:
        return await service.modify(session, activity_id, activity)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete("/{activity_id}")
async def delete_activity(
    activity_id: int,
    session: AsyncSession = Depends(database.scoped_session_dependency),
):
    try:
        return await service.delete(session, activity_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
