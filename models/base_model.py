#!/usr/bin/python3
"""
    File: base_model.py
"""
from uuid import uuid4
from datetime import datetime


class BaseModel(object):
    """BaseModel Class Definition"""

    def __init__(self, *args, **kwargs):
        """Initialization Method"""
        self.id = str(uuid4())
        self.updated_at = datetime.today()
        self.created_at = datetime.today()
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """String representation of self"""
        name = self.__class__.__name__
        return '[{}] ({}) {}'.format(name, self.id, self.__dict__)

    def save(self):
        """saves with the current date time"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """ returns a __dict__ of the instance"""
        td = self.__dict__.copy()
        td["created_at"] = self.created_at.isoformat()
        td["updated_at"] = self.updated_at.isoformat()
        td["__class__"] = self.__class__.__name__
        return td
