#!/usr/bin/python3
"""
    File: test_amenity.py
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity testing class"""

    def test_blank(self):
        x = Amenity()
        self.assertIsInstance(x.name, str)
