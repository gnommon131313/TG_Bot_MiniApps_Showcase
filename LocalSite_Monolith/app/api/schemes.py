from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    description: str | None = Field(max_length=100)
    price: int = Field(ge=0)
    
    
class CreateOrder(BaseModel):
    product_id: int
    user_id: int