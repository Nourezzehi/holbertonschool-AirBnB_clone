#!/usr/bin/python3
"""Test Case For Base Model"""

from models.base_model import BaseModel
from models import storage
import unittest
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Create an base of BAseModel for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """check the base"""
        self.assertIsInstance(self.model, BaseModel)

    def test_init(self):
        """Test __init__"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))
    
    def test_str(self):
        """Test the __str__ method"""
        expected_str = "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__
        )
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """Test the save method"""
        obj = BaseModel(id='test_id', attribute1='value1', attribute2='value2')
        storage.__objects = {'BaseModel.test_id': obj}
        storage.__file_path = 'test_file.json'

    def test_to_dict(self):
        """Tests the dict method"""
        obj = BaseModel()
        new_dict = obj.__dict__.copy()
        new_dict["__class__"] = obj.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        comparing = obj.to_dict()
        self.assertDictEqual(new_dict, comparing)


if __name__ == '__main__':
    unittest.main
