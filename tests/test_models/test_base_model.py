#!/usr/bin/python3
"""Test Case For Base Model"""

from models.base_model import BaseModel
import unittest
from datetime import datetime



class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Create an instance of BAseModel for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """check the instance"""
        self.assertIsInstance(self.model, BaseModel)

    def test_init(self):
        """Test that the constructor method"""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_init_with_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-01T12:30:00.000000',
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(model.updated_at, datetime(2023, 1, 1, 12, 30, 0))
        self.assertEqual(model.custom_attr, 'custom_value')


    def test_str(self):
        """Test the __str__ method"""
        expected_str = "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__
        )
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """Test the save method"""
        updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'],
                         self.model.__class__.__name__)
        self.assertEqual(
            model_dict['created_at'],
            self.model.created_at.isoformat())
        self.assertEqual(
            model_dict['updated_at'],
            self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main
