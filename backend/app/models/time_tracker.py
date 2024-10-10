from datetime import datetime

from pydantic import BaseModel


class ActivityRecordDB(BaseModel):
    id: int
    color: str
    type: str
    interval: int
    date: datetime


class ActivityRecord(BaseModel):
    color: str
    type: str
    interval: int
    date: datetime


class ActivityStatistic(BaseModel):
    activies: list[ActivityRecord]
    interval: int
