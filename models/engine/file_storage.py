from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    # Add all classes to this dictionary
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        from json import dump
        with open(self.__file_path, "w") as f:
            dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        from json import load
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = load(f)
            for key, value in obj_dict.items():
                cls_name = value["__class__"]
                cls = self.classes.get(cls_name)
                if cls:
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
