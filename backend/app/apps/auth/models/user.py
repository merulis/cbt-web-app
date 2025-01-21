from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


if TYPE_CHECKING:
    from app.activity.models.activity import Activity
    from app.auth.models.profile import Profile


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    passhash: Mapped[str]

    activies: Mapped[list["Activity"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")
