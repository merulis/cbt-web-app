from fastapi import (
    APIRouter,
    Depends,
)

from app.apps.auth.service import jwt
from app.apps.auth import validation

from app.apps.users.schemas import (
    UserSchema,
    TokenInfo,
    TokenPayload,
    UserInfo,
)

from fastapi.security import HTTPBearer

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(prefix="/auth", dependencies=[Depends(http_bearer)])


@router.post("/login/", response_model=TokenInfo)
def auth_user(user: UserSchema = Depends(validation.validate_user)):
    access_token = jwt.create_access_token(user)
    refresh_token = jwt.create_refresh_token(user)
    return TokenInfo(access_token=access_token, refresh_token=refresh_token)


@router.post("/token/refresh/", response_model=TokenInfo)
def refresh_jwt(
    user: UserSchema = Depends(jwt.get_currnet_auth_user_for_refresh),
):
    access_token = jwt.create_access_token(user)
    refresh_token = jwt.create_refresh_token(user)
    return TokenInfo(access_token=access_token, refresh_token=refresh_token)


@router.get("/user/me/")
def auth_user_check_self_info(
    payload: TokenPayload = Depends(jwt.get_currnet_token_payload),
    user: UserSchema = Depends(jwt.get_currnet_active_user),
):
    return UserInfo(
        username=user.username,
        email=user.email,
        logget_at=payload.iat,
    )
