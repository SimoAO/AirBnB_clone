#!/usr/bin/python3
"""Unittest for user """
from models.user import User
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ test the user"""
    def test_user_id(self):
        """test the unique id"""
        my_user1 = User()
        my_user2 = User()
        self.assertNotEqual(my_user1.id, my_user2.id)

    def test_user__str__(self):
        """ test the str methode """
        my_user1 = User()
        self.assertEqual(type(my_user1.__str__()), str)
        self.assertIn("[User]", my_user1.__str__())
        self.assertIn("id", my_user1.__str__())
        self.assertIn("created_at", my_user1.__str__())
        self.assertIn("updated_at", my_user1.__str__())
        self.assertEqual(type(my_user1.id), str)
        self.assertEqual(type(my_user1.created_at), datetime)
        self.assertEqual(type(my_user1.updated_at), datetime)
        self.assertEqual(type(my_user1.email), str)
        self.assertEqual(type(my_user1.password), str)
        self.assertEqual(type(my_user1.first_name), str)
        self.assertEqual(type(my_user1.last_name), str)
        my_user1.num = 89
        self.assertEqual(type(my_user1.num), int)

        self.assertTrue(hasattr(my_user1, "email"))
        self.assertTrue(hasattr(my_user1, "password"))
        self.assertTrue(hasattr(my_user1, "first_name"))
        self.assertTrue(hasattr(my_user1, "last_name"))

    def test_user_save(self):
        """Test the save method"""
        my_user1 = User()
        original_updated_at = my_user1.updated_at
        my_user1.save()
        self.assertNotEqual(original_updated_at, my_user1.updated_at)

    def test_user_to_dict(self):
        """Test the to_dict method"""
        my_user1 = User()
        my_user1.email = "abdo@gmail.com"
        my_user1.password = "hgtyuil"
        my_user1.first_name = "abdo"
        my_user1.last_name = "jojo"
        my_model_dict = my_user1.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('email', my_model_dict)
        self.assertIn('password', my_model_dict)
        self.assertIn('first_name', my_model_dict)
        self.assertIn('last_name', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()
