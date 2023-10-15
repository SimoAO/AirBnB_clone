#!/usr/bin/python3
"""Unittest for City """
from models.city import City
import unittest
from datetime import datetime


class TestCity(unittest.TestCase):
    """ test the City"""
    def test_City_id(self):
        """test the unique id"""
        my_City1 = City()
        my_City2 = City()
        self.assertNotEqual(my_City1.id, my_City2.id)

    def test_City__str__(self):
        """ test the str methode """
        my_City1 = City()
        self.assertEqual(type(my_City1.__str__()), str)
        self.assertIn("[City]", my_City1.__str__())
        self.assertIn("id", my_City1.__str__())
        self.assertIn("created_at", my_City1.__str__())
        self.assertIn("updated_at", my_City1.__str__())
        self.assertEqual(type(my_City1.id), str)
        self.assertEqual(type(my_City1.created_at), datetime)
        self.assertEqual(type(my_City1.updated_at), datetime)
        self.assertEqual(type(my_City1.name), str)

        my_City1.num = 89
        self.assertEqual(type(my_City1.num), int)

        self.assertTrue(hasattr(my_City1, "name"))
        self.assertTrue(hasattr(my_City1, "state_id"))

    def test_City_save(self):
        """Test the save method"""
        my_City1 = City()
        original_updated_at = my_City1.updated_at
        my_City1.save()
        self.assertNotEqual(original_updated_at, my_City1.updated_at)

    def test_City_to_dict(self):
        """Test the to_dict method"""
        my_City1 = City()
        my_City1.name = "abdo"
        my_model_dict = my_City1.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'City')


if __name__ == '__main__':
    unittest.main()
