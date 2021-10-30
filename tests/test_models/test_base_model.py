#!/usr/bin/python3
"""
    File: test_base_model.py
"""
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_creation(unittest.TestCase):
    """Testing creation for __init__ of BaseModel"""

    def test_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids(self):
        base_a = BaseModel()
        base_b = BaseModel()
        self.assertNotEqual(base_a.id, base_b.id)

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    def test_save_none(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)

    def test_save_update(self):
        base = BaseModel()
        base.save()
        baseid = "BaseModel." + base.id
        with open("file.json", "r") as fd:
            self.assertIn(baseid, fd.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_type(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_output(self):
        today = datetime.today()
        base = BaseModel()
        base.id = "43435"
        base.created_at = base.updated_at = today
        a = {
            'id': '43435',
            '__class__': 'BaseModel',
            'created_at': today.isoformat(),
            'updated_at': today.isoformat()
        }
        self.assertDictEqual(base.to_dict(), a)

    def test_none_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)


if __name__ == "__main__":
    unittest.main()
