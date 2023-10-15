#!/usr/bin/python3
"""Unittest for Amenity """
from models.amenity import Amenity
import unittest
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ test the Amenity"""
    def test_Amenity_id(self):
        """test the unique id"""
        my_Amenity1 = Amenity()
        my_Amenity2 = Amenity()
        self.assertNotEqual(my_Amenity1.id, my_Amenity2.id)

    def test_Amenity__str__(self):
        """ test the str methode """
        my_Amenity1 = Amenity()
        self.assertEqual(type(my_Amenity1.__str__()), str)
        self.assertIn("[Amenity]", my_Amenity1.__str__())
        self.assertIn("id", my_Amenity1.__str__())
        self.assertIn("created_at", my_Amenity1.__str__())
        self.assertIn("updated_at", my_Amenity1.__str__())
        self.assertEqual(type(my_Amenity1.id), str)
        self.assertEqual(type(my_Amenity1.created_at), datetime)
        self.assertEqual(type(my_Amenity1.updated_at), datetime)
        self.assertEqual(type(my_Amenity1.name), str)

        my_Amenity1.num = 89
        self.assertEqual(type(my_Amenity1.num), int)

        self.assertTrue(hasattr(my_Amenity1, "name"))

    def test_Amenity_save(self):
        """Test the save method"""
        my_Amenity1 = Amenity()
        original_updated_at = my_Amenity1.updated_at
        my_Amenity1.save()
        self.assertNotEqual(original_updated_at, my_Amenity1.updated_at)

    def test_Amenity_to_dict(self):
        """Test the to_dict method"""
        my_Amenity1 = Amenity()
        my_Amenity1.name = "abdo"
        my_model_dict = my_Amenity1.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
