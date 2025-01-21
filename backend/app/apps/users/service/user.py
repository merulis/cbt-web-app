from sqlalchemy.ext.asyncio import AsyncSession

from app.apps.auth.repository import user as db

from app.apps.users.schemas import User, UserCreate, UserUpdate


def get_all() -> list[User]:
    return db.get_users()


def get_one(
    session: AsyncSession,
    user_id: int,
) -> User:
    return db.get_user(
        session=session,
        user_id=user_id,
    )


def create(session: AsyncSession, user: UserCreate) -> User:
    return db.create_user(
        session=session,
        user_create=user,
    )


def modify(session: AsyncSession, user: User, user_update: UserUpdate) -> User:
    return db.update_user(
        session=session,
        user_in=user,
        user_update=user,
    )


def delete(session: AsyncSession, user: User) -> bool:
    return db.delete_user(
        session=session,
        user_delete=user,
    )
