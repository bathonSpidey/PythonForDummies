import unittest

from src.Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 3), 5)