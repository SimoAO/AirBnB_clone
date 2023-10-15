#!/usr/bin/python3
"""Unittest for base_model """
from models.base_model import BaseModel
import unittest


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
        print(type(my_model1.__str__()))

        self.assertEqual(type(my_model1.__str__()), str)
        self.assertIn("[BaseModel]", my_model1.__str__())
        self.assertIn("id", my_model1.__str__())
        self.assertIn("created_at", my_model1.__str__())
        self.assertIn("updated_at", my_model1.__str__())
        self.assertEqual(type(my_model1.id), str)
        print(type(my_model1.created_at))
        self.assertEqual(type(my_model1.created_at), str)
        self.assertEqual(type(my_model1.updated_at), str)
        my_model1.num = 89
        self.assertEqual(type(my_model1.num), int)


if __name__ == '__main__':
    unittest.main()
