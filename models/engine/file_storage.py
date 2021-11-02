#!/usr/bin/python3
"""
    File: file_storage.py
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage(object):
    """FileStorage class definition"""

    __file_path = "file.json"
    __objects = {}
    class_list = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "Review": Review, "City": City, "Amenity": Amenity, "Place": Place
    }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        x = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as fd:
            for key, value in FileStorage.__objects.items():
                x.update({key: value.to_dict()})
            fd.write(json.dumps(x))

    def reload(self):
        try:
            with open(self.__file_path, mode='r') as fd:
                nd = json.load(fd)
            for key in nd:
                self.__objects[key] = self.class_list[nd[key]
                                                      ["__class__"]](**nd[key])
        except BaseException:
            pass
