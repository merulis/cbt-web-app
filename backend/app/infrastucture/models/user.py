# from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import (
    String,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.infrastucture.db.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    role: Mapped[str] = mapped_column(
        String(24),
        default="new_user",
    )
