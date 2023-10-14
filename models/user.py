#!/usr/bin/python3
""" scribt for the class user that defines
    all common attributes/methods for other classe
"""
from models.base_model import BaseModel


class User(BaseModel):
    """sub class of BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
