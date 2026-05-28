from fastapi import APIRouter, Depends

from src.app.products.dependencies import get_product_service

from src.app.products.schemas import ProductCreate, ProductResponse
from src.app.products.service import ProductService

from src.app.core.security.roles import require_owner

product_router = APIRouter(prefix="/product", tags=["Products"])


@product_router.post("/", response_model=ProductResponse)
def create_product(
    data: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    return service.create_product(data)
