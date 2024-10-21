import asyncio

from datetime import timedelta

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import database, User, Profile, Activity


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print("user", user)
    return user


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User | None:
    stmt = select(User).where(User.username == username)
    user: User | None = await session.scalar(stmt)
    print(f"Found user {username}: {user}")
    return user


async def create_profile(
    session: AsyncSession,
    user_id: int,
    fname: str | None = None,
    lname: str | None = None,
    bio: str | None = None,
) -> Profile:
    profile = Profile(user_id=user_id, first_name=fname, last_name=lname, bio=bio)
    session.add(profile)
    await session.commit()

    return profile


async def show_users_and_profile(session: AsyncSession):
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    users = await session.scalars(stmt)

    for user in users:
        print(user)
        if user.profile:
            print(user.profile)


async def create_activity(
    session: AsyncSession,
    user_id: int,
    *activies_in: str,
) -> list[Activity]:
    activies = [
        Activity(
            color=color,
            category=category,
            interval=timedelta(days=interval),
            date=database.now(),
            user_id=user_id,
        )
        for color, category, interval, _ in activies_in
    ]

    return activies


async def main():
    async with database.session_factory() as session:
        await show_users_and_profile(session)


if __name__ == "__main__":
    asyncio.run(main())
