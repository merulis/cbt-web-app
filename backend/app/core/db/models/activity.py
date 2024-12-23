from typing import TYPE_CHECKING

from datetime import datetime, timedelta

from sqlalchemy.orm import Mapped

from .base import Base
from .mixins import UserRelationMixin


if TYPE_CHECKING:
    pass


class Activity(UserRelationMixin, Base):
    _user_back_populates = "activies"

    color: Mapped[str]
    category: Mapped[str]
    interval: Mapped[timedelta]
    date: Mapped[datetime]
