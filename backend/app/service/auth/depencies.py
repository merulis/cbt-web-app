from datetime import timedelta

from app.service.auth.validation import (
    validate_token_payload,
    validate_token_type,
)
from app.service.auth.crud import user_db as db
from app.core.settings import settings
from app.core import security

from jwt.exceptions import ExpiredSignatureError

from fastapi import (
    HTTPException,
    Depends,
    status,
)

from fastapi.security import OAuth2PasswordBearer

from app.schemas.user import (
    UserSchema,
    TokenPayload,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")


def create_jwt(
    token_type: str,
    payload: dict,
    expires_minutes: int | None = None,
    expire_timedelta: timedelta | None = None,
):
    jwt_payload = {"token_type": token_type}
    jwt_payload.update(payload)

    return security.encode_jwt(
        payload=jwt_payload,
        expire_minutes=expires_minutes,
        expire_timedelta=expire_timedelta,
    )


# FIXME: now we passing username in sub, it need to change on id
def create_access_token(
    user: UserSchema,
) -> str:
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }

    return create_jwt(
        token_type=settings.JWT.ACCESS_TYPE,
        payload=jwt_payload,
        expires_minutes=settings.JWT.ACCESS_TOKEN_EXPIRE_MINUTES,
    )


# FIXME: now we passing username in sub, it need to change on id
def create_refresh_token(
    user: UserSchema,
) -> str:
    jwt_payload = {
        "sub": user.username,
    }

    expire = timedelta(days=settings.JWT.REFRESH_TOKEN_EXPIRE_DAYS)

    return create_jwt(
        token_type=settings.JWT.REFRESH_TYPE,
        payload=jwt_payload,
        expire_timedelta=expire,
    )


def get_currnet_token_payload(
    token: str = Depends(oauth2_scheme),
) -> TokenPayload:
    try:
        payload: dict = security.decode_jwt(
            token=token,
        )

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
        )

    validate_payload = validate_token_payload(payload)

    return validate_payload


def get_user_by_token_sub(
    payload: TokenPayload = Depends(get_currnet_token_payload),
):
    username: str = payload.sub
    if user := db.get(username):
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalid",
    )


def get_currnet_auth_user(
    payload: TokenPayload = Depends(get_currnet_token_payload),
) -> UserSchema:
    validate_token_type(payload, settings.JWT.ACCESS_TYPE)
    return get_user_by_token_sub(payload=payload)


def get_currnet_auth_user_for_refresh(
    payload: TokenPayload = Depends(get_currnet_token_payload),
) -> UserSchema:
    validate_token_type(payload, settings.JWT.REFRESH_TYPE)
    return get_user_by_token_sub(payload=payload)


def get_currnet_active_user(
    user: UserSchema = Depends(get_currnet_auth_user),
) -> UserSchema:
    if user.active:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User inactive",
    )
