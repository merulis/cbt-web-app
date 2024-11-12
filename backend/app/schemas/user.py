from typing import Literal, Union

from pydantic import BaseModel
from pydantic import EmailStr, Field

from datetime import datetime


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=32)
    email: EmailStr
    passhash: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: bytes
    active: bool = True


class UserInfo(BaseModel):
    username: str
    email: EmailStr
    logget_at: datetime


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"


class AccessTokenPayload(BaseModel):
    token_type: Literal["access"]
    sub: int
    username: str
    email: EmailStr
    exp: datetime
    iat: datetime


class RefreshTokenPayload(BaseModel):
    token_type: Literal["refresh"]
    sub: int
    exp: datetime
    iat: datetime


TokenPayload = Union[AccessTokenPayload, RefreshTokenPayload]
