import unittest
from datetime import datetime
from uuid import UUID

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

        # Verificar que el valor de 'id' es un UUID válido
        self.assertIsInstance(UUID(model_dict['id']), UUID)

    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        self.assertIsInstance(model_str, str)
        self.assertIn('BaseModel', model_str)
        self.assertIn(model.id, model_str)
        self.assertIn(str(model.__dict__), model_str)


if __name__ == '__main__':
    unittest.main()
