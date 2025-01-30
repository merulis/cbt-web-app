from dataclasses import dataclass, field

from uuid import UUID
from datetime import datetime


@dataclass
class User:
    id: UUID
    email: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    role: str | None = None

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
