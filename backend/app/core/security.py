import jwt
import bcrypt

from app.core.settings import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.JWT.PRIVATE_KEY.read_text(),
    algorithm: str = settings.JWT.ALGORITHM,
):
    encoded = jwt.encode(
        payload=payload,
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
