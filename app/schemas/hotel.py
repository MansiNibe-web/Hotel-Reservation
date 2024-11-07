from pydantic import BaseModel
from typing import Optional

class HotelCreate(BaseModel):
    branch: str
    pincode: str
    locality: str
    manager: str

class HotelUpdate(BaseModel):
    branch: Optional[str] = None
    pincode: Optional[str] = None
    locality: Optional[str] = None
    manager: Optional[str] = None


class HotelResponse(HotelCreate):
    id: int

    class Config:
        from_attributes = True