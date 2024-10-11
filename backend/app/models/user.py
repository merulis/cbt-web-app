from pydantic import BaseModel
from pydantic import EmailStr, Field


class NewUser(BaseModel):
    username: str = Field(..., min_length=3, max_length=32)
    email: EmailStr
    hash: str


class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=32)
    email: EmailStr
    hash: str
