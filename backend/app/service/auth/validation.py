from app.core import security as auth
from app.core.settings import settings
from app.schemas.user import (
    AccessTokenPayload,
    RefreshTokenPayload,
    TokenPayload,
)

from app.service.auth.crud import user_db as db
from fastapi import Form, HTTPException, status
from pydantic import ValidationError


def validate_user(
    username: str = Form(),
    password: str = Form(),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid user or password",
    )

    if not (user := db.get(username)):
        raise unauthed_exc

    if not auth.validate_password(
        password=password,
        hash=user.password,
    ):
        raise unauthed_exc

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User inactive",
        )

    return user


def validate_token_payload(payload: dict) -> TokenPayload:
    try:
        token_type = payload.get("token_type")
        if token_type == settings.JWT.ACCESS_TYPE:
            validate_payload = AccessTokenPayload.model_validate(
                obj=payload,
            )

        if token_type == settings.JWT.REFRESH_TYPE:
            validate_payload = RefreshTokenPayload.model_validate(
                obj=payload,
            )

    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication error, invalid token",
        )

    return validate_payload
