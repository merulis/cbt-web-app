from datetime import datetime

from pydantic import BaseModel, Field


class ActivityRecord(BaseModel):
    color: str
    type: str
    interval: datetime
    date: datetime


class ActivityStatistic(BaseModel):
    activies: list[ActivityRecord]
    interval: datetime
