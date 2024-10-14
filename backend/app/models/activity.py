from datetime import datetime

from pydantic import BaseModel


class ActivityRecord(BaseModel):
    id: int
    color: str
    type: str
    interval: int
    date: datetime


class NewActivityRecord(BaseModel):
    color: str
    type: str
    interval: int
    date: datetime


class ActivityStatistic(BaseModel):
    activies: list[ActivityRecord]
    interval: int
