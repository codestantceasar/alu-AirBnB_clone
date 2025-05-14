#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, State)

if __name__ == "__main__":
    unittest.main()
