#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_storage_instance(self):
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

if __name__ == "__main__":
    unittest.main()
