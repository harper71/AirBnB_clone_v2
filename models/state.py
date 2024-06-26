#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Column, String
from models.base_model import BaseModel
from models.base_model import Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(60), nullable=False)
