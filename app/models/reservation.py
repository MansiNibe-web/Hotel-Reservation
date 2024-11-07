# from sqlalchemy import Column, Integer, ForeignKey, String
# from sqlalchemy.orm import relationship
# from app.database import Base

# class Reservation(Base):
#     __tablename__ = "reservations"
    
#     id = Column(Integer, primary_key=True, index=True)
#     room_id = Column(Integer, ForeignKey("rooms.id"))
#     customer_id = Column(Integer, ForeignKey("customers.id"))
#     check_in_date = Column(String(255))  # Use date or datetime in production
#     check_out_date = Column(String(255))
    
#     customer = relationship("Customer", back_populates="reservations")
#     room = relationship("Room")
