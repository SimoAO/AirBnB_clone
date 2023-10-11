#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """sub class of BaseModel """
    name = ""