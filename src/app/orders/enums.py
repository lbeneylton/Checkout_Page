from enum import Enum


class OrderStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    canceled = "canceled"
