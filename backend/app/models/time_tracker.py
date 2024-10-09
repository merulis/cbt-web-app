from datetime import datetime, timedelta

from pydantic import BaseModel


class ActivityRecord(BaseModel):
    id: int
    color: str
    type: str
    interval: timedelta
    date: datetime


class ActivityStatistic(BaseModel):
    activies: list[ActivityRecord]
    interval: timedelta
