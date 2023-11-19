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
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with a specified key"""
        new_obj = "{}.{}".format(type(obj).__name__,
                                 obj.id)
        FileStorage.__objects[new_obj] = obj

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
                for value in temp.values():
                    self.new(BaseModel(**value))
        except FileNotFoundError:
            pass
