from app.schemas.user import UserSchema, TokenPayload

from jwt.exceptions import ExpiredSignatureError
from pydantic import ValidationError

from fastapi import (
    Form,
    HTTPException,
    Depends,
    status,
)
from fastapi.security import OAuth2PasswordBearer

from app.core import security as auth


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")

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
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User inactive",
        )

    return user


def get_currnet_token_payload(
    token: str = Depends(oauth2_scheme),
) -> TokenPayload:
    try:
        payload = auth.decode_jwt(
            token=token,
        )
        validate_payload = TokenPayload.model_validate(payload)

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication error",
        )

    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication error",
        )

    else:
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
