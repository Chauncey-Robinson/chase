from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..schemas.order import OrderOut
from ..models.order import Order
from ..db.database import SessionLocal

router = APIRouter()

@router.get("/orders/", response_model=List[OrderOut])
def get_orders(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    orders = db.query(Order).offset(skip).limit(limit).all()
    return orders
