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

    def __str__(self):
        """String representation of self"""
        name = self.__class__.__name__
        return '[{}] ({}) {}'.format(name, self.id, self.__dict__)
