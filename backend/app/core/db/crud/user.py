from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import User

from app.schemas.user import UserCreate, UserUpdate


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    activies = list(result.scalars().all())
    return activies


async def get_user(
    session: AsyncSession,
    user_id: int,
) -> User | None:
    return await session.get(User, user_id)


async def create_user(
    session: AsyncSession,
    user_create: UserCreate,
) -> User:
    record = user_create.model_dump()
    user = User(**record)
    session.add(user)

    await session.commit()
    await session.refresh(user)

    return user


async def update_user(
    session: AsyncSession,
    user_in: User,
    user_update: UserUpdate,
) -> User:
    for key, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user_in, key, value)

    await session.commit()
    await session.refresh(user_in)

    return user_in


async def delete_user(
    session: AsyncSession,
    user_delete: User,
) -> None:
    await session.delete(user_delete)
    await session.commit()
