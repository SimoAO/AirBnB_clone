#!/usr/bin/python3
"""Unittest for Review """
from models.review import Review
import unittest
from datetime import datetime


class TestReview(unittest.TestCase):
    """ test the Review"""
    def test_Review_id(self):
        """test the unique id"""
        my_Review1 = Review()
        my_Review2 = Review()
        self.assertNotEqual(my_Review1.id, my_Review2.id)

    def test_Review__str__(self):
        """ test the str methode """
        my_Review1 = Review()
        self.assertEqual(type(my_Review1.__str__()), str)
        self.assertIn("[Review]", my_Review1.__str__())
        self.assertIn("id", my_Review1.__str__())
        self.assertIn("created_at", my_Review1.__str__())
        self.assertIn("updated_at", my_Review1.__str__())
        self.assertEqual(type(my_Review1.id), str)
        self.assertEqual(type(my_Review1.created_at), datetime)
        self.assertEqual(type(my_Review1.updated_at), datetime)
        self.assertEqual(type(my_Review1.place_id), str)
        self.assertEqual(type(my_Review1.user_id), str)
        self.assertEqual(type(my_Review1.text), str)

        my_Review1.num = 89
        self.assertEqual(type(my_Review1.num), int)

        self.assertTrue(hasattr(my_Review1, "place_id"))
        self.assertTrue(hasattr(my_Review1, "user_id"))
        self.assertTrue(hasattr(my_Review1, "text"))

    def test_Review_save(self):
        """Test the save method"""
        my_Review1 = Review()
        original_updated_at = my_Review1.updated_at
        my_Review1.save()
        self.assertNotEqual(original_updated_at, my_Review1.updated_at)

    def test_Review_to_dict(self):
        """Test the to_dict method"""
        my_Review1 = Review()
        my_Review1.name = "abdo"
        my_model_dict = my_Review1.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'Review')


if __name__ == '__main__':
    unittest.main()
