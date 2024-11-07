# Import CRUD operations for each model
# In app/crud/__init__.py

from .hotel import create_hotel, get_hotel, update_hotel, delete_hotel
from .room import create_room, get_room, update_room, delete_room, get_room_by_id
from .customer import create_customer, get_customer, update_customer, delete_customer, get_or_create_hotel
# from .reservation import create_reservation, get_reservation, update_reservation, delete_reservation
from app import models
