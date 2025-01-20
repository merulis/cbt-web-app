from sqlalchemy.ext.asyncio import AsyncSession

from app.activity.repository import activity as db
from app.activity.schemas.activity import (
    Activity,
    ActivityCreate,
    ActivityUpdatePartial,
)

from app.db.exceptions import Missing


async def get_all(
    session: AsyncSession,
) -> list[Activity]:
    return await db.get_activies(session)


async def get_one(
    session: AsyncSession,
    activity_id: int,
) -> Activity:
    activity = await db.get_activity(session, activity_id)
    if activity:
        return activity

    raise Missing(msg=f"Activity id={activity_id} not found")


async def create(
    session: AsyncSession,
    activity_in: ActivityCreate,
) -> ActivityCreate:
    return await db.create_activity(
        session=session,
        activity_create=activity_in,
    )


async def update(
    session: AsyncSession,
    activity_in: Activity,
    activity_update: ActivityUpdatePartial,
) -> Activity:
    return await db.update_activity(
        session=session,
        activity_in=activity_in,
        activity_update=activity_update,
    )


async def delete(
    session: AsyncSession,
    activity_delete: Activity,
) -> None:
    await db.delete_activity(
        session=session,
        activity_delete=activity_delete,
    )
