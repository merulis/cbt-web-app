from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ActivityCreate(BaseModel):
    color: str
    type: str
    interval: int
    date: datetime


class ActivityCreate(ActivityCreate):
    pass


class Activity(ActivityCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ActivityStatistic(BaseModel):
    activies: list[Activity]
    interval: int
