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


class User(BaseModel):
    id: int
