from datetime import datetime

from sqlalchemy import String, DateTime, Integer, func
from sqlalchemy.orm import Mapped, mapped_column

from src.app.database.base import Base


class User(Base):
    """
    user_id : int primary key
    email: str unique not null
    password_hash: str not null
    """

    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
