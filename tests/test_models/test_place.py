#!/usr/bin/python3
"""Unittest for Place """
from models.place import Place
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ test the Place"""
    def test_Place_id(self):
        """test the unique id"""
        my_Place1 = Place()
        my_Place2 = Place()
        self.assertNotEqual(my_Place1.id, my_Place2.id)

    def test_Place__str__(self):
        """ test the str methode """
        my_Place1 = Place()
        self.assertEqual(type(my_Place1.__str__()), str)
        self.assertIn("[Place]", my_Place1.__str__())
        self.assertIn("id", my_Place1.__str__())
        self.assertIn("created_at", my_Place1.__str__())
        self.assertIn("updated_at", my_Place1.__str__())
        self.assertEqual(type(my_Place1.id), str)
        self.assertEqual(type(my_Place1.created_at), datetime)
        self.assertEqual(type(my_Place1.updated_at), datetime)
        self.assertEqual(type(my_Place1.name), str)

        my_Place1.num = 89
        self.assertEqual(type(my_Place1.num), int)

        self.assertTrue(hasattr(my_Place1, "name"))

    def test_Place_save(self):
        """Test the save method"""
        my_Place1 = Place()
        original_updated_at = my_Place1.updated_at
        my_Place1.save()
        self.assertNotEqual(original_updated_at, my_Place1.updated_at)

    def test_Place_to_dict(self):
        """Test the to_dict method"""
        my_Place1 = Place()
        my_Place1.name = "abdo"
        my_model_dict = my_Place1.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'Place')


if __name__ == '__main__':
    unittest.main()
