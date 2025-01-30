from dataclasses import (
    dataclass,
    asdict,
    field,
)
from enum import Enum

from datetime import datetime, timedelta
from app.config import settings


class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"


@dataclass
class BaseJWTPayload:
    sub: str
    role: str
    iat: datetime = field(default_factory=datetime.now)

    def to_dict(self):
        return asdict(self)


@dataclass
class AccessJWTPayload(BaseJWTPayload):
    jtt: TokenType = TokenType.ACCESS
    exp: datetime = field(
        default_factory=lambda: datetime.now()
        + timedelta(minutes=settings.JWT.ACCESS_TOKEN_EXPIRE_MINUTES),
    )


@dataclass
class RefreshJWTPayload(BaseJWTPayload):
    jtt: TokenType = TokenType.REFRESH
    exp: datetime = field(
        default_factory=lambda: datetime.now()
        + timedelta(days=settings.JWT.REFRESH_TOKEN_EXPIRE_DAYS),
    )
