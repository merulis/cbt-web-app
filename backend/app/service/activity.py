from sqlalchemy.ext.asyncio import AsyncSession

from app.exeptions.data import Missing
from app.data.crud import activity as db
from app.schemas.activity import Activity, ActivityCreate


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

    raise Missing(msg=f"Activity id: {id} not found")


async def create(
    session: AsyncSession,
    activity_in: ActivityCreate,
) -> ActivityCreate:
    return await db.create_activity(session, activity_in)


async def update(
    session: AsyncSession,
    activity_in: Activity,
    activity_update: ActivityCreate,
) -> Activity:
    return await db.update_activity(session, activity_in, activity_update)


async def delete(
    session: AsyncSession,
    activity_in: int,
) -> None:
    await db.delete_activity(activity_in)
