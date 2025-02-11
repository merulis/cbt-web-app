from typing import Protocol

from dataclasses import (
    dataclass,
    asdict,
    field,
)
from enum import Enum

from datetime import datetime, timedelta
from app.config import config


class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"


class JWTPayloadSchema(Protocol):
    def to_dict(self) -> dict:
        pass


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
        + timedelta(minutes=config.JWT.ACCESS_TOKEN_EXPIRE_MINUTES),
    )


@dataclass
class RefreshJWTPayload(BaseJWTPayload):
    jtt: TokenType = TokenType.REFRESH
    exp: datetime = field(
        default_factory=lambda: datetime.now()
        + timedelta(days=config.JWT.REFRESH_TOKEN_EXPIRE_DAYS),
    )
