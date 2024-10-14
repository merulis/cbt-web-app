from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.data import Activity

from app.models.activity import ActivityCreate


async def get_activies(session: AsyncSession) -> list[Activity]:
    stmt = select(Activity).order_by(Activity.id)
    result: Result = await session.execute(stmt)
    activies = list(result.scalars().all())
    return activies


async def get_activity(
    session: AsyncSession,
    activity_id: int,
) -> Activity | None:
    return await session.get(Activity, activity_id)


async def create_activity(
    session: AsyncSession,
    data: ActivityCreate,
) -> Activity:
    activity = Activity(**data.model_dump())
    session.add(activity)

    await session.commit()
    await session.refresh(activity)
