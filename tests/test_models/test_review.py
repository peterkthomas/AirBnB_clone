#!/usr/bin/python3
"""
    File: test_review.py
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review testing class"""

    def test_blank(self):
        x = Review()
        self.assertIsInstance(x.place_id, str)
        self.assertIsInstance(x.user_id, str)
        self.assertIsInstance(x.text, str)
