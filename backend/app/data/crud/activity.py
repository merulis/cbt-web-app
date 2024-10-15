from datetime import datetime
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.data import Activity

from app.schemas.activity import ActivityCreate, ActivityUpdatePartial


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
    activity_in: ActivityCreate,
) -> Activity:
    record = activity_in.model_dump()
    date: datetime = record.get("date")
    record.update({"date": date.replace(tzinfo=None)})

    activity = Activity(**record)
    session.add(activity)

    await session.commit()
    await session.refresh(activity)

    return activity


async def update_activity(
    session: AsyncSession,
    activity: Activity,
    activity_update: ActivityUpdatePartial,
) -> Activity:
    for key, value in activity_update.model_dump(exclude_unset=True).items():
        setattr(activity, key, value)

    await session.commit()
    await session.refresh(activity)

    return activity


async def delete_activity(
    session: AsyncSession,
    activity: Activity,
) -> None:
    await session.delete(activity)
    await session.commit()
