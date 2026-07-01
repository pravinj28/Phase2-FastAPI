from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):

    name: str 
    price: float
    quantity : int
    description : Optional[str] = None

p = Product(name = "Pravin", price = 10.2, quantity = 1)
print(p)
print(p.model_dump())