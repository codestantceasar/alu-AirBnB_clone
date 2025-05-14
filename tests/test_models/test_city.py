#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, City)

if __name__ == "__main__":
    unittest.main()
