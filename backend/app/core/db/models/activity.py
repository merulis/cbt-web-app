from datetime import datetime, timedelta

from sqlalchemy.orm import Mapped

from app.core.db import Base


class Activity(Base):

    color: Mapped[str]
    type: Mapped[str]
    interval: Mapped[timedelta]
    date: Mapped[datetime]
