#!/usr/bin/python3
"""objects to a file"""

import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON
    file to instances"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with a specified key"""
        new_obj = "{}.{}".format(type(obj).__name__,
                                 obj.id)
        self.__objects[new_obj] = obj

    def save(self):
        """Saves storage dictionary to file"""

        temp = {}
        temp = FileStorage.__objects.copy()
        for key, val in temp.items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    class_name = value['__class__']
                    # Assuming classes are in the global scope
                    class_obj = globals()[class_name]
                    instance = class_obj(**value)
                    self.all()[key] = instance
        except FileNotFoundError:
            pass
