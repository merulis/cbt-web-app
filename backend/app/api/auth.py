from fastapi import (
    APIRouter,
    Depends,
)

from app.service.auth import depencies as service
from app.service.auth import validation

from app.schemas.user import (
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
    access_token = service.create_access_token(user)
    refresh_token = service.create_refresh_token(user)
    return TokenInfo(access_token=access_token, refresh_token=refresh_token)


@router.post("/token/refresh/", response_model=TokenInfo)
def refresh_jwt(
    user: UserSchema = Depends(service.get_currnet_auth_user_for_refresh),
):
    access_token = service.create_access_token(user)
    refresh_token = service.create_refresh_token(user)
    return TokenInfo(access_token=access_token, refresh_token=refresh_token)


@router.get("/user/me/")
def auth_user_check_self_info(
    payload: TokenPayload = Depends(service.get_currnet_token_payload),
    user: UserSchema = Depends(service.get_currnet_active_user),
):
    return UserInfo(
        username=user.username,
        email=user.email,
        logget_at=payload.iat,
    )
