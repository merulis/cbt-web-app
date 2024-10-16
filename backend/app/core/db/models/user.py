from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


if TYPE_CHECKING:
    from .activity import Activity
    from .profile import Profile


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)

    activies: Mapped[list["Activity"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")
