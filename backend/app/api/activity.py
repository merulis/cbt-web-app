from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status

from app.data import database

from app.service import activity as service
from app.schemas.activity import (
    Activity,
    ActivityCreate,
    ActivityUpdatePartial,
)

from .dependencies import activity


router = APIRouter(prefix="/activity")


@router.get("/")
async def get_activies(
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> list[Activity]:
    return await service.get_all(session=session)


@router.get("/{activity_id}")
async def get_activity(
    activity: Activity = Depends(activity.get_activity_by_id),
) -> Activity:
    return activity


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_activity(
    activity_in: ActivityCreate,
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> Activity:
    return await service.create(
        session=session,
        activity_in=activity_in,
    )


@router.patch("/{activity_id}")
async def update_activity(
    activity_update: ActivityUpdatePartial,
    activity: Activity = Depends(activity.get_activity_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> Activity:
    return await service.update(
        session=session,
        activity_in=activity,
        activity_update=activity_update,
    )


@router.delete(
    "/{activity_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_activity(
    activity: Activity = Depends(activity.get_activity_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> None:
    await service.delete(
        session=session,
        activity_delete=activity,
    )
