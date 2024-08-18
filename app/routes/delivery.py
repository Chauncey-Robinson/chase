from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.delivery import DeliveryCreate, DeliveryOut
from ..models.delivery import Delivery
from ..db.database import SessionLocal

router = APIRouter()

@router.post("/deliveries/", response_model=DeliveryOut)
def create_delivery(delivery: DeliveryCreate, db: Session = Depends(SessionLocal)):
    db_delivery = Delivery(**delivery.dict())
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery
