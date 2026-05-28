from fastapi import Depends
from infra.database.dependency import get_session

from src.app.products.repository import ProductRepository
from src.app.products.service import ProductService


def get_product_repository(session=Depends(get_session)):
    return ProductRepository(session)


def get_product_service(
    repository: ProductRepository = Depends(get_product_repository)
) -> ProductService:
    return ProductService(repository)
