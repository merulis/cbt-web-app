from sqlalchemy.ext.asyncio import AsyncSession

from app.data.crud import activity as db_crud
from app.schemas.activity import Activity, ActivityCreate


async def get_all(
    session: AsyncSession,
) -> list[Activity]:
    return await db_crud.get_activies(session)


async def get_one(
    session: AsyncSession,
    activity_id: int,
) -> Activity:
    return await db_crud.get_activity(session, activity_id)


async def create(
    session: AsyncSession,
    activity: ActivityCreate,
) -> ActivityCreate:
    pass


def modify(
    session: AsyncSession,
    activity_id: int,
    activity: ActivityCreate,
) -> Activity:
    pass


def delete(
    session: AsyncSession,
    activity_id: int,
) -> bool:
    pass
