#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ class that create a BaseModel """
    def __init__(self, *args, **kwargs):
        """ initialize a BaseModel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    format_t = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, format_t)
                elif (key != "__class__"):
                    self.__dict__[key] = value
        else:
            models.storage.new(self)


    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance:"""
        dict_2 = self.__dict__.copy()
        
        dict_2["created_at"] = self.created_at.isoformat()
        dict_2["updated_at"] = self.updated_at.isoformat()
        dict_2["__class__"] = self.__class__.__name__
        return dict_2
    

