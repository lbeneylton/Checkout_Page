from datetime import datetime
from enum import Enum

from sqlalchemy import String, DateTime, ForeignKey, func, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.database.base import Base


class PaymentStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"


class BillingType(str, Enum):
    pix = "PIX"
    credit_card = "CREDIT_CARD"


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"),
        nullable=False
    )

    asaas_payment_id: Mapped[str] = mapped_column(
        String(255),
        nullable=True  # pode não existir antes do gateway responder
    )

    status: Mapped[PaymentStatus] = mapped_column(
        SAEnum(PaymentStatus, name="payment_status"),
        nullable=False,
        default=PaymentStatus.pending
    )

    billing_type: Mapped[BillingType] = mapped_column(
        SAEnum(BillingType, name="billing_type"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # relacionamento
    order = relationship("Order")
