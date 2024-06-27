#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Column, String, BaseModel
from sqlalchemy.orm import relationship
from models.base_model import Base
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(60), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delet, delete-orphan', passive_deletes=True)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            import models
            from models.city import City
            cities_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
