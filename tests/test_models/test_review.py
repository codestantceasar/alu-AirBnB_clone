#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)

if __name__ == "__main__":
    unittest.main()
