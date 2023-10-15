#!/usr/bin/python3
"""Unittest for Filestorage """
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """ test the Filestorage"""
    def test_all(self):
        """ test the all methode"""
        self.assertEqual(type(models.storage.all()), dict)

    def test_new(self):
        """ test the new methode"""
        mymodel = BaseModel()
        models.storage.new(mymodel)
        self.assertIn(mymodel, models.storage.all().values())
        self.assertIn("BaseModel." + mymodel.id, models.storage.all().keys())

    def test_save(self):
        """ test the save methode"""
        mc = BaseModel()
        models.storage.new(mc)
        models.storage.save()
        with open("file.json", "r") as f:
            file_data = f.read()
            self.assertIn("BaseModel." + mc.id, file_data)

    def test_reload(self):
        """ test the reload methode"""
        mc = BaseModel()
        models.storage.new(mc)
        models.storage.save()
        models.storage.reload()
        objs = models.storage.all()
        self.assertIn("BaseModel." + mc.id, objs)


if __name__ == '__main__':
    unittest.main()
