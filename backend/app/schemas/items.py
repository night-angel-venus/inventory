from pydantic import BaseModel, ConfigDict
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    price: int
    stock: int

class ItemResponse(BaseModel):
    id: int
    name: str
    price: int
    stock: int

    model_config = ConfigDict(from_attributes=True)

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    stock: Optional[int] = None