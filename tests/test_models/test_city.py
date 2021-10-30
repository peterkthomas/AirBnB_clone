#!/usr/bin/python3
"""
    File: test_city.py
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Testing City Class"""

    def test_blank(self):
        city = City()
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)
