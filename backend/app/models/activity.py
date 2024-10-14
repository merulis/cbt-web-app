from datetime import datetime

from pydantic import BaseModel


class ActivityBase(BaseModel):
    color: str
    type: str
    interval: int
    date: datetime


class Activity(ActivityBase):
    id: int


class ActivityStatistic(BaseModel):
    activies: list[Activity]
    interval: int
