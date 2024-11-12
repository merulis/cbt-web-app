from app.schemas.user import UserSchema, TokenPayload

from jwt.exceptions import InvalidTokenError
from fastapi import (
    Form,
    HTTPException,
    Depends,
    status,
)

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core import security as auth


http_bearer = HTTPBearer()

john = UserSchema(
    id=1,
    username="John",
    password=auth.hash_password("qwerty"),
    email="john@example.com",
    active=True,
)

sam = UserSchema(
    id=2,
    username="Sam",
    password=auth.hash_password("secret"),
    email="sam@example.com",
    active=True,
)

user_db: dict[str, UserSchema] = {
    john.username: john,
    sam.username: sam,
}


def validate_user(
    username: str = Form(),
    password: str = Form(),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid user or password",
    )

    if not (user := user_db.get(username)):
        raise unauthed_exc

    if not auth.validate_password(
        password=password,
        hash=user.password,
    ):
        raise unauthed_exc

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User inactive"
        )

    return user


def get_currnet_token_payload(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> TokenPayload:
    token = credentials.credentials
    try:
        payload = auth.decode_jwt(
            token=token,
        )
        validate_payload = TokenPayload.model_validate(payload)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={f"Invalid token {e}"},
        )

    return validate_payload


def get_currnet_user(
    payload: dict = Depends(get_currnet_token_payload),
) -> UserSchema:
    username: str = payload.username
    if user := user_db.get(username):
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalid",
    )


def get_currnet_active_user(
    user: UserSchema = Depends(get_currnet_user),
) -> UserSchema:
    if user.active:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User inactive",
    )
