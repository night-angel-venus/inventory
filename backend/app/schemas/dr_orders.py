from pydantic import BaseModel, ConfigDict
from datetime import date as date_type
from typing import Optional

class DROrderCreate(BaseModel):
    order_no: str
    date: date_type

class DROrderResponse(BaseModel):
    id: int
    order_no: str
    date: date_type

    model_config = ConfigDict(from_attributes=True)

class DROrderUpdate(BaseModel):
    order_no: Optional[str] = None
    date: Optional[date_type] = None