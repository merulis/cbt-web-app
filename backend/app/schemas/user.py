from pydantic import BaseModel
from pydantic import EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=32)
    email: EmailStr
    passhash: str


class UserCreate(UserBase):
    ...


class UserUpdate(UserBase):
    ...


class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: bytes
    active: bool = True


class TokenInfo(BaseModel):
    access_token: str
    token_type: str
