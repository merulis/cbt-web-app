from datetime import datetime

from pydantic import BaseModel


class ThoughtBase(BaseModel):
    author: str
    situation: str
    auto_thought: str
    cognitive_distortion_type: str
    alternative_thought: str
    create: datetime


class ThoughtCreate(ThoughtBase):
    ...


class ThoughtUpdate(ThoughtBase):
    ...


class Thought(ThoughtBase):
    id: int
