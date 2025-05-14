#!/usr/bin/python3
"""FileStorage class module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Serializes and deserializes objects to/from JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                from models import base_model
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = val["__class__"]
                    self.__objects[key] = eval(cls_name)(**val)
        except FileNotFoundError:
            pass
