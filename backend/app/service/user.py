import os
import secrets

from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError

from app.schemas.user import NewUser, User

if os.getenv("UNIT_TEST"):
    pass
else:
    from app.data import user as data

from passlib.context import CryptContext


SECRET_KEY = secrets.token_hex(16)
ALGORITM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)


def get_hash(plain: str) -> str:
    return pwd_context.hash(plain)


def get_jwt_username(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITM])
        if not (username := payload.get("sub")):
            return None
    except JWTError:
        return None
    return username


def get_current_user(token: str) -> User | None:
    if not (id_ := get_jwt_username(token)):
        return None
    if user := lookup_user(id_):
        return user
    return None


def lookup_user(id_: int) -> User | None:
    if user := data.get_one():
        return user
    return None


def auth_user(id_: int, plain: str) -> User | None:
    if not (user := lookup_user(id_)):
        return None
    if not verify_password(plain, user.hash):
        return None
    return None


def create_access_token(data: dict, expires: timedelta | None = None):
    src = data.copy()
    now = datetime.now()
    if not expires:
        expires = timedelta(minutes=15)
    src.update({"exp": now + expires})
    encoded_jwt = jwt.encode(src, SECRET_KEY, algorithm=[ALGORITM])
    return encoded_jwt


def get_all() -> list[User]:
    return data.get_all()


def get_one(id_: int) -> User:
    return data.get_one(id_)


def create(user: NewUser) -> User:
    return data.create(user)


def modify(id_: int, user: NewUser) -> User:
    return data.modify(id_, user)


def delete(id_: int) -> bool:
    return data.delete(id_)
