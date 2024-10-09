from pydantic import BaseModel
from pydantic import EmailStr, Field


class NewUser(BaseModel):
    username: str = Field(..., min_length=3, max_length=32)
    email: EmailStr
    password: str = Field(..., min_length=4, max_length=32)
