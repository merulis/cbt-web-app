from dataclasses import dataclass

from datetime import datetime


@dataclass
class Activity:
    id: int
    title: str
    start_time: datetime
    end_time: datetime
    desctiption: str | None = None

    def duration(self):
        pass

    def validate_time(self):
        pass
