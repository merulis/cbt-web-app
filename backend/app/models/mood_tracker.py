from datetime import datetime

from pydantic import BaseModel, Field


class MoodRecord(BaseModel):
    color: str
    type: str
    date: datetime


class MoodStatistic(BaseModel):
    moods: list[MoodRecord]
    interval: datetime
