from pydantic import BaseModel, ConfigDict
from datetime import date as date_type
from typing import Optional

class StockOutCreate(BaseModel):
    dr_id: int
    item_id: int
    quantity: int 

class StockOutResponse(BaseModel):
    id: int
    dr_id: int
    item_id: int
    quantity: int 

    model_config = ConfigDict(from_attributes=True)

class StockOutUpdate(BaseModel):
    dr_id: Optional[int] = None
    item_id: Optional[int] = None
    quantity: Optional[int] = None 