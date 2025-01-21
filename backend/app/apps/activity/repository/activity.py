from datetime import datetime
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import Activity

from app.activity.schemas.activity import ActivityCreate, ActivityUpdatePartial


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
    activity_create: ActivityCreate,
) -> Activity:
    record = activity_create.model_dump()
    date: datetime = record.get("date")
    record.update({"date": date.replace(tzinfo=None)})

    activity = Activity(**record)
    session.add(activity)

    await session.commit()
    await session.refresh(activity)

    return activity


async def update_activity(
    session: AsyncSession,
    activity_in: Activity,
    activity_update: ActivityUpdatePartial,
) -> Activity:
    for key, value in activity_update.model_dump(exclude_unset=True).items():
        setattr(activity_in, key, value)

    await session.commit()
    await session.refresh(activity_in)

    return activity_in


async def delete_activity(
    session: AsyncSession,
    activity_delete: Activity,
) -> None:
    await session.delete(activity_delete)
    await session.commit()
