#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)

if __name__ == "__main__":
    unittest.main()
