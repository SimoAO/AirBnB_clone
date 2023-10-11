#!/usr/bin/python3
"""Unittest for base_model """



from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """ test the base model"""
    def test_base_model_id(self):
        my_model = BaseModel()
        print(my_model.id)



if __name__ == '__main__':
    unittest.main()
