#!/usr/bin/python3
"""Test Case For Base Model"""

from models.base_model import BaseModel
from models import FileStorage
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Create an instance of BaseModel for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """Check the base"""
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
    obj.created_at = datetime.now()

    file_storage = FileStorage()
    file_storage._FileStorage__objects = {'BaseModel.test_id': obj}
    file_storage._FileStorage__file_path = 'test_file.json'
    file_storage.save()


    def test_to_dict(self):
        """Tests the to_dict method"""
        obj = BaseModel()
        new_dict = obj.__dict__.copy()
        new_dict["__class__"] = obj.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        comparing = obj.to_dict()
        self.assertDictEqual(new_dict, comparing)


if __name__ == '__main__':
    unittest.main()
