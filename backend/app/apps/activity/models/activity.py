from typing import TYPE_CHECKING

from datetime import datetime, timedelta

from sqlalchemy.orm import Mapped

from app.db.base import Base
from app.apps.users.mixins import UserRelationMixin


if TYPE_CHECKING:
    pass


class Activity(UserRelationMixin, Base):
    _user_back_populates = "activies"

    color: Mapped[str]
    category: Mapped[str]
    interval: Mapped[timedelta]
    date: Mapped[datetime]
