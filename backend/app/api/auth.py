from fastapi import (
    APIRouter,
    Depends,
)

from app.core import security as auth
from app.service import auth as service
from app.schemas.user import UserSchema, TokenInfo, TokenPayload


router = APIRouter(prefix="/auth")


@router.post("/login/", response_model=TokenInfo)
def auth_user(user: UserSchema = Depends(service.validate_user)):
    jwt_payload = {
        "sub": user.id,
        "username": user.username,
        "email": user.email,
    }
    access_token = auth.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=access_token,
        token_type="Bearer",
    )


@router.get("/user/me/")
def auth_user_check_self_info(
    payload: TokenPayload = Depends(service.get_currnet_token_payload),
    user: UserSchema = Depends(service.get_currnet_active_user),
):
    return {"username": user.username, "email": user.email, "logget_in_at": payload.iat}
