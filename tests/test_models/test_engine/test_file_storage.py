#!/usr/bin/python3
"""
    File: test_file_storage.py
"""
import unittest
import json


class TestFileStorage(unittest.TestCase):
    """File Storage Test"""

    def test_json_load(self):
        with open("file.json") as fd:
            d = json.load(fd)
            self.assertEqual(isinstance(d, dict), True)

    def test_file(self):
        with open("file.json") as fd:
            self.assertTrue(len(fd.read()) > 0)


if __name__ == '__main__':
    unittest.main()
