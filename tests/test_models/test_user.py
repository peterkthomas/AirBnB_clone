#!/usr/bin/python3
"""
    File: test_user.py
"""
import unittest
import models
from models.user import User


class TestUser(unittest.TestCase):
    """User testing class"""

    def test_blank(self):
        x = User()
        self.assertIsInstance(x.email, str)
        self.assertIsInstance(x.password, str)
        self.assertIsInstance(x.first_name, str)
        self.assertIsInstance(x.last_name, str)


if __name__ == "__main__":
    unittest.main()
