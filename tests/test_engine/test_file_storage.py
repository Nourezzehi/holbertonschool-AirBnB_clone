import unittest
from models import FileStorage, BaseModel
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up a file path and create a FileStorage instance"""
        self.file_path = 'test_file.json'
        self.file_storage = FileStorage()

    def test_base_model_save(self):
        base = BaseModel()
        self.assertTrue(os.path.exists('file.json'))

    def to_dict(self):
        base = FileStorage()
        self.assertEqual(type(base.to_dict()), dict)

if __name__ == '__main__':
    unittest.main()
