#!/usr/bin/python3
"""
    File: file_storage.py
"""
import json
import models


class FileStorage(object):
    """FileStorage class definition"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        x = {}
        with open(self.__file_path, mode='w') as fd:
            for key, value in FileStorage.__objects.items():
                x.update({key: value.to_dict()})
            fd.write(json.dumps(x))

    def reload(self):
        try:
            with open(self.__file_path, mode='r') as fd:
                nd = json.loads(fd)
                for key in nd:
                    self.__objects[key] = getattr(
                        models, nd[key]['__class__'])(
                        **nd[key])
        except Exception:
            pass
