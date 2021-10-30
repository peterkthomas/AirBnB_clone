#!/usr/bin/python3
"""
    File: test_place.py
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Place testing class"""

    def test_blank(self):
        x = Place()
        self.assertIsInstance(x.city_id, str)
        self.assertIsInstance(x.user_id, str)
        self.assertIsInstance(x.name, str)
        self.assertIsInstance(x.description, str)
        self.assertIsInstance(x.number_rooms, int)
        self.assertIsInstance(x.number_bathrooms, int)
        self.assertIsInstance(x.max_guest, int)
        self.assertIsInstance(x.price_by_night, int)
        self.assertIsInstance(x.latitude, float)
        self.assertIsInstance(x.longitude, float)
        self.assertIsInstance(x.amenity_ids, list)
