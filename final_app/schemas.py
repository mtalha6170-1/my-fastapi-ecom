from pydantic import BaseModel 
from typing import Optional 

class ProductBase(BaseModel):
    title : str
    description : Optional[str] = None
    price : float
    stock_quantity : int
    category_id: int


class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int



    class Config:
        from_attributes = True


