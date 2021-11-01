#!/usr/bin/python3
"""
    File: test_state.py
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """State testing class"""

    def test_blank(self):
        x = State()
        self.assertIsInstance(x.name, str)
