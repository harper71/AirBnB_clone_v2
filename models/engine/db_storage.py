#!/usr/bin/python3
"""creates a class to assign data to
the DATABASE with Sqlalcemey
"""

import os
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """handles the database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the database storage"""

        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        Env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, database, pool_pre_ping=True))
        
        if Env == 'test':
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """Add the object to the database session (self.__session)"""

        objects = {}
        if cls:
            for object in self.__session.query(cls).all():
                key = f'{cls.__name__}.{object.id}'
            objects[key] = object
        else:
            for cls_name in Base._decl_class_registry.values():
                if isinstance(cls_name, type):
                    for obj in self.__session.query(cls_name).all():
                        key = f'{object.__class__.__name__}.{object.id}'
                        objects[key] = object
        return objects

    def new(self, obj):
        """adds the object to the current database session """
        self.__session.all(obj)
    
    def save(self):
        """commit all changes of the current database"""

        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database session"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
