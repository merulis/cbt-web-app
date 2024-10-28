from datetime import datetime, timedelta

import jwt
import bcrypt

from app.core.settings import settings


def encode_expire(
    payload: dict,
    expire_minutes: int = settings.JWT.ACCESS_TOKEN_EXPIRE_MINUTES,
    expire_timedelta: timedelta | None = None,
):
    to_encode = payload.copy()
    now = datetime.now()

    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)

    to_encode.update(
        exp=expire,
        iat=now,
    )

    return to_encode


def encode_jwt(
    payload: dict,
    private_key: str = settings.JWT.PRIVATE_KEY.read_text(),
    algorithm: str = settings.JWT.ALGORITHM,
    expire_minutes: int = settings.JWT.ACCESS_TOKEN_EXPIRE_MINUTES,
    expire_timedelta: timedelta | None = None,
):
    payload_with_expire = encode_expire(
        payload=payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta,
    )

    encoded = jwt.encode(
        payload=payload_with_expire,
        key=private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.JWT.PUBLIC_KEY.read_text(),
    algorithm: str = settings.JWT.ALGORITHM,
):
    decoded = jwt.decode(
        jwt=token,
        key=public_key,
        algorithm=[algorithm],
    )
    return decoded


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pw: bytes = password.encode()
    return bcrypt.hashpw(password=pw, salt=salt)


def validate_password(
    password: str,
    hash: bytes,
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hash,
    )
