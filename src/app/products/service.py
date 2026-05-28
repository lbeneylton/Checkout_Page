from src.app.products.repository import ProductRepository
from src.app.products.models import Product

from src.app.core.exceptions import ConflictError


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def _exists_product(self, name: str) -> None:
        if self.repository.get_active_by_name(name.strip().lower()):
            raise ConflictError("Já existe um produto com esse nome")

    def create_product(self, data) -> Product:
        self._exists_product(data.name)

        product = Product(
            name=data.name,
            description=data.description,
            price=data.price
        )

        product_created = self.repository.create(product)

        self.repository.session.commit()
        self.repository.session.refresh(product_created)

        return product_created
