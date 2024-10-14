from datetime import datetime

from pydantic import BaseModel


class MoodBase(BaseModel):
    color: str
    type: str
    date: datetime


class MoodCreate(MoodBase):
    pass


class Mood(MoodBase):
    id: int


class MoodStatistic(BaseModel):
    moods: list[Mood]
    interval: datetime
