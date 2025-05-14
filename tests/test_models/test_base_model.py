#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_id_is_str(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_created_at_is_datetime(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_updated_at_is_datetime(self):
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
