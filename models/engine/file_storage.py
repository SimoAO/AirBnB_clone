#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes:

models/base_model.py"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User" : User,
        "State" : State,
        "City" : City,
        "Amenity" : Amenity,
        "Place" : Place,
        "Review" : Review,
    }

    def all(sef):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj


    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        serialized_objects = {}
        for key ,value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing.
          If the file doesn't exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as f:
               loaded = json.load(f)
               for key, val in loaded.items():
                    base = FileStorage.classes[val["__class__"]](**val)
                    FileStorage.__objects[key] = base
                   
               #print(loaded)
        except FileNotFoundError:
            return