from dataclasses import dataclass, field, asdict

from datetime import datetime


@dataclass
class UserEntity:
    id: int
    email: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    role: str | None = None

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def to_dict(self):
        return asdict(self)
