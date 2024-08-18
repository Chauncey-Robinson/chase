from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..db.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    delivery_status = Column(String, index=True)
    delivery_time = Column(DateTime)
    created_at = Column(DateTime)

    user = relationship("User", back_populates="orders")
