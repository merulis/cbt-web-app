from datetime import timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.crud import user as data

from app.schemas.user import User, UserCreate, UserUpdate


def verify_password(plain: str, hash: str) -> bool:
    ...


def get_hash(plain: str) -> str:
    ...


def get_jwt_username(token: str) -> str | None:
    ...


def get_current_user(token: str) -> User | None:
    ...


def lookup_user(id_: int) -> User | None:
    ...


def auth_user(id_: int, plain: str) -> User | None:
    ...


def create_access_token(
    data: dict,
    expires: timedelta | None = None,
):
    ...


def get_all() -> list[User]:
    return data.get_users()


def get_one(
    session: AsyncSession,
    user_id: int,
) -> User:
    return data.get_user(
        session=session,
        user_id=user_id,
    )


def create(session: AsyncSession, user: UserCreate) -> User:
    return data.create_user(
        session=session,
        user_create=user,
    )


def modify(session: AsyncSession, user: User, user_update: UserUpdate) -> User:
    return data.update_user(
        session=session,
        user_in=user,
        user_update=user,
    )


def delete(session: AsyncSession, user: User) -> bool:
    return data.delete_user(
        session=session,
        user_delete=user,
    )
