#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Column, String
from sqlalchemy import ForeignKey
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('state_id'), unique=True, nullable=False)
    name = Column(String(128), nullable=False)
