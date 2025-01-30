from dataclasses import dataclass

from uuid import UUID
from datetime import datetime


@dataclass
class Activity:
    id: UUID
    title: str
    start_time: datetime
    end_time: datetime
    desctiption: str | None = None

    def duration(self):
        pass

    def validate_time(self):
        pass
