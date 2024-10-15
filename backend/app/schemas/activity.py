from datetime import datetime, timedelta

from pydantic import BaseModel, ConfigDict


class ActivityCreate(BaseModel):
    color: str
    type: str
    interval: timedelta
    date: datetime


class ActivityCreate(ActivityCreate):
    ...


class ActivityUpdatePartial(BaseModel):
    color: str | None = None
    type: str | None = None
    interval: timedelta | None = None
    date: datetime | None = None


class Activity(ActivityCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ActivityStatistic(BaseModel):
    activies: list[Activity]
    interval: int
