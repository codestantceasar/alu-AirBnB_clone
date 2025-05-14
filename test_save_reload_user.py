#!/usr/bin/env python3
"""
Test for save and reload functionality of User class
"""

import unittest
import os
from models import storage
from models.user import User

class TestUserSaveReload(unittest.TestCase):
    def setUp(self):
        """Set up a clean test environment"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "john.doe@example.com"
        self.user.password = "pass123"
        self.user.save()

    def tearDown(self):
        """Clean up the created file and objects"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_user_saved_and_reloaded(self):
        """Test if user is saved to and reloaded from file storage"""
        user_id = self.user.id

        # Clear in-memory objects
        storage._FileStorage__objects.clear()

        # Reload from file
        storage.reload()

        key = f"User.{user_id}"
        self.assertIn(key, storage.all())
        reloaded_user = storage.all()[key]
        self.assertEqual(reloaded_user.first_name, "John")
        self.assertEqual(reloaded_user.last_name, "Doe")
        self.assertEqual(reloaded_user.email, "john.doe@example.com")
        self.assertEqual(reloaded_user.password, "pass123")

if __name__ == '__main__':
    unittest.main()
