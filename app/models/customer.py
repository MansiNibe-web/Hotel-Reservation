from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    
    phone_number = Column(String(255), primary_key=True, unique=True, index=True)
    
    name = Column(String(255), index=True)
    age = Column(Integer, nullable=False, index=True)
    email = Column(String(255), unique=True, index=True)
    traveling_from = Column(String(100), nullable=True, index=True)
    isForeign = Column(Boolean, default=False)
    purpose = Column(String(200), nullable=False, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))

    room = relationship("Room", back_populates="customers")

    