from pydantic import BaseModel, Field
from decimal import Decimal


class ProductCreate(BaseModel):
    """
    nome: str

    description: str

    price: str ge 0
    """

    name: str
    description: str
    price: Decimal = Field(
        ge=0,
        description="Preço do produto"
    )


class ProductResponse(BaseModel):
    product_id: int
    name: str
