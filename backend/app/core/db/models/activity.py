from datetime import datetime, timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Activity(Base):
    color: Mapped[str]
    type: Mapped[str]
    interval: Mapped[timedelta]
    date: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
    )
