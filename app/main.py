from fastapi import FastAPI
from app.database import engine, Base
from app.routers import hotel_router, room_router, customer_router

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(hotel_router, prefix="/hotels", tags=["hotels"])
app.include_router(room_router, prefix="/rooms", tags=["rooms"])
app.include_router(customer_router, prefix="/customers", tags=["customers"])
# app.include_router(reservation_router, prefix="/reservations", tags=["reservations"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)
