# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.models.reservation import Reservation
# from app.schemas.reservation import ReservationBase
# from app.database import get_db

# router = APIRouter()

# @router.post("/", response_model=ReservationBase)
# def create_reservation(reservation: ReservationBase, db: Session = Depends(get_db)):
#     db_reservation = Reservation(room_id=reservation.room_id, customer_id=reservation.customer_id, check_in_date=reservation.check_in_date, check_out_date=reservation.check_out_date)
#     db.add(db_reservation)
#     db.commit()
#     db.refresh(db_reservation)
#     return db_reservation

# @router.get("/{reservation_id}", response_model=ReservationBase)
# def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
#     reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
#     if not reservation:
#         raise HTTPException(status_code=404, detail="Reservation not found")
#     return reservation

# @router.put("/{reservation_id}", response_model=ReservationBase)
# def update_reservation(reservation_id: int, reservation: ReservationBase, db: Session = Depends(get_db)):
#     db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
#     if not db_reservation:
#         raise HTTPException(status_code=404, detail="Reservation not found")
#     db_reservation.room_id = reservation.room_id
#     db_reservation.customer_id = reservation.customer_id
#     db_reservation.check_in_date = reservation.check_in_date
#     db_reservation.check_out_date = reservation.check_out_date
#     db.commit()
#     db.refresh(db_reservation)
#     return db_reservation

# @router.delete("/{reservation_id}")
# def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
#     reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
#     if not reservation:
#         raise HTTPException(status_code=404, detail="Reservation not found")
#     db.delete(reservation)
#     db.commit()
#     return {"detail": "Reservation deleted"}
