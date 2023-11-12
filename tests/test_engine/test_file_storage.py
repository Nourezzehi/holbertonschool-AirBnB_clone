#!/usr/bin/python3
"""Unittest for FileStorage Class"""


import unittest
from datetime import datetime
import models
BaseModel = models.base_model.BaseModel
from models.engine.file_storage import FileStorage
storage = models.storage


def setUp(self):
    """This method is called before each test"""
    FileStorage.__objects = {}


def test_all(self):
    file_storage = FileStorage()
    result = file_storage.all()
    self.assertEqual(result, {})


def test_new(self):
    file_storage = FileStorage()
    obj = BaseModel(id='obj_id')
    file_storage.new(obj)
    result = file_storage.all()
    key = "BaseModel.obj_id"
    self.assertIn(key, result)
    self.assertEqual(result[key], obj)

def test_save_and_reload(self):
    file_storage = FileStorage()
    obj = BaseModel(id='obj_id')
    file_storage.new(obj)
    file_storage.save()
    file_storage.reload()
    result = file_storage.all()
    key = "BaseModel.obj_id"
    self.assertIn(key, result)
    self.assertEqual(result[key].id, obj.id)

if __name__ == '__main__':
    unittest.main()
