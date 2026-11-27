from pydantic import BaseModel, ConfigDict
from datetime import date as date_type
from typing import Optional

class BaseStockCreate(BaseModel):
    item_id: int
    quantity: int

class BaseStockResponse(BaseModel):
    id: int
    item_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)

class BaseStockUpdate(BaseModel):
    item_id: Optional[int] = None 
    quantity: Optional[int] = None 