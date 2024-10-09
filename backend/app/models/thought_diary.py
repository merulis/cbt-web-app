from datetime import datetime

from pydantic import BaseModel


class ThoughtRecord(BaseModel):
    id: int
    author: str
    situation: str
    auto_thought: str
    cognitive_distortion_type: str
    alternative_thought: str
    create: datetime
