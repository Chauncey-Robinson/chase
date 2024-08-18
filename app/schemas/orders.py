from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    delivery_id: int
    status: str
    created_at: Optional[datetime] = None

class OrderCreate(OrderBase):
    pass  # No additional fields are needed for creating an order

class OrderOut(OrderBase):
    id: int

    class Config:
        orm_mode = True  # This is important to allow SQLAlchemy models to be returned as Pydantic models
