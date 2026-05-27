from datetime import datetime, UTC

from sqlalchemy.orm import Session
from sqlalchemy import select

from src.app.products.models import Product


class ProductRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def _active_only(self):
        return select(Product).where(Product.deleted_at.is_(None))

    def create(self, product: Product):
        self.session.add(product)
        return product

    def get_active_by_id(self, product_id: int) -> Product | None:
        return self.session.execute(
            self._active_only()
            .where(Product.product_id == product_id)
        ).scalar_one_or_none()

    def list_active(self):
        return self.session.execute(
            self._active_only()
            .order_by(Product.created_at)
        ).scalars().all()

    def delete(self, user_id: int):  # sem commit
        user = self.get_active_by_id(user_id)

        if not user:
            return None

        user.deleted_at = datetime.now(UTC)
        self.session.add(user)
        return user
