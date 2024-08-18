from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserOut
from ..models.user import User
from ..db.database import SessionLocal
from ..utils.security import hash_password

router = APIRouter()

@router.post("/register/", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
