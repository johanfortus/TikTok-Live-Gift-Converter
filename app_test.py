from app import app, diamond_converter
from unittest import TestCase

class diamondConverterTestCase(TestCase):
    def test_diamond_converter(self):
        self.assertEqual(diamond_converter(1), 0.05)
        