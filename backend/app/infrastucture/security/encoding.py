from datetime import datetime, timedelta, timezone

import jwt
import bcrypt

from app.config import config


def _encode_expire(
    payload: dict,
    expire_minutes: int = config.JWT.ACCESS_TOKEN_EXPIRE_MINUTES,
    expire_timedelta: timedelta | None = None,
):
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)

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
    private_key: str = config.JWT.PRIVATE_KEY.read_text(),
    algorithm: str = config.JWT.ALGORITHM,
    expire_minutes: int = config.JWT.ACCESS_TOKEN_EXPIRE_MINUTES,
    expire_timedelta: timedelta | None = None,
):
    payload_with_expire = _encode_expire(
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
    public_key: str = config.JWT.PUBLIC_KEY.read_text(),
    algorithms: list[str] = [config.JWT.ALGORITHM],
):
    decoded = jwt.decode(
        jwt=token,
        key=public_key,
        algorithms=algorithms,
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
