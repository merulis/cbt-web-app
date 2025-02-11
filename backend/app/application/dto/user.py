from dataclasses import (
    dataclass,
    field,
    asdict,
)

from datetime import datetime


@dataclass
class UserDTO:
    username: str
    email: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    role: str | None = None

    def to_dict(self):
        return asdict(self)
