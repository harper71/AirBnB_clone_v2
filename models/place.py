#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import ForeignKey, Column, String, Integer, Float
from models.base_model import Base

class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Custom(String(60), ForeignKey(cities.id), nullable=False)
    user_id = Custom(String(60), ForeignKey(users.id), nullable=False)
    name = Custom(String(128), nullable=False)
    description = Custom(String(128), nullable=False)
    number_rooms = Custom(Integer, nullable=False, default=0)
    number_bathrooms = Custom(Integer, nullable=False, default=0)
    max_guest = Custom(Integer, nullable=False, default=0)
    price_by_night = Custom(Integer, nullable=False, default=0)
    latitude = Custom(Float, nullable=True)
    longitude = Custom(Float, nullable=True)
    amenity_ids = []
