from datetime import datetime

from pydantic import BaseModel, Field


class ThoughtRecord(BaseModel):
    id: int
    author: str
    situation: str
    auto_thought: str
    cognitive_distortion_type: str
    create: datetime
