#!/usr/bin/python3
"""Unittest for state """
from models.state import State
import unittest
from datetime import datetime


class TestState(unittest.TestCase):
    """ test the state"""
    def test_state_id(self):
        """test the unique id"""
        my_State1 = State()
        my_State2 = State()
        self.assertNotEqual(my_State1.id, my_State2.id)

    def test_State__str__(self):
        """ test the str methode """
        my_State1 = State()
        self.assertEqual(type(my_State1.__str__()), str)
        self.assertIn("[State]", my_State1.__str__())
        self.assertIn("id", my_State1.__str__())
        self.assertIn("created_at", my_State1.__str__())
        self.assertIn("updated_at", my_State1.__str__())
        self.assertEqual(type(my_State1.id), str)
        self.assertEqual(type(my_State1.created_at), datetime)
        self.assertEqual(type(my_State1.updated_at), datetime)
        self.assertEqual(type(my_State1.name), str)

        my_State1.num = 89
        self.assertEqual(type(my_State1.num), int)

        self.assertTrue(hasattr(my_State1, "name"))

    def test_State_save(self):
        """Test the save method"""
        my_State1 = State()
        original_updated_at = my_State1.updated_at
        my_State1.save()
        self.assertNotEqual(original_updated_at, my_State1.updated_at)

    def test_State_to_dict(self):
        """Test the to_dict method"""
        my_State1 = State()
        my_State1.name = "abdo"
        my_model_dict = my_State1.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()
