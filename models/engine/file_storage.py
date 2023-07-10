#!/usr/bin/python3
"""
serialization and deserialization of json file instances
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """storage class initialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    attributeValue = eval(value["__class__"])(**value)
                    self.__objects[key] = attributeValue
        except FileNotFoundError:
            pass
