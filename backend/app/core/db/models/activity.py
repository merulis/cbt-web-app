from typing import TYPE_CHECKING

from datetime import datetime, timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from .user import User


class Activity(Base):
    color: Mapped[str]
    type: Mapped[str]
    interval: Mapped[timedelta]
    date: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
    )

    user: Mapped["User"] = relationship(back_populates="activies")
