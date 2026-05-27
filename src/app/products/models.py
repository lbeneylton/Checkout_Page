from src.app.database.base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, String, func, Numeric

from datetime import datetime
from decimal import Decimal


class Product(Base):

    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
