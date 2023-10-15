#!/usr/bin/python3
"""Unittest for base_model """
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ test the base model"""
    def test_base_model_id(self):
        """test the unique id"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_base_model__str__(self):
        """ test the str methode """
        my_model1 = BaseModel()
        # print(type(my_model1.__str__()))

        self.assertEqual(type(my_model1.__str__()), str)
        self.assertIn("[BaseModel]", my_model1.__str__())
        self.assertIn("id", my_model1.__str__())
        self.assertIn("created_at", my_model1.__str__())
        self.assertIn("updated_at", my_model1.__str__())
        self.assertEqual(type(my_model1.id), str)
        # print(type(my_model1.created_at))
        self.assertEqual(type(my_model1.created_at), datetime)
        self.assertEqual(type(my_model1.updated_at), datetime)
        my_model1.num = 89
        self.assertEqual(type(my_model1.num), int)

    def test_base_model_save(self):
        """Test the save method"""
        my_model1 = BaseModel()
        original_updated_at = my_model1.updated_at
        my_model1.save()
        self.assertNotEqual(original_updated_at, my_model1.updated_at)

    def test_base_model_to_dict(self):
        """Test the to_dict method"""
        my_model1 = BaseModel()
        my_model_dict = my_model1.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
