import unittest

from src.Calculator import Calculator


class TestAverges(unittest.TestCase):
    def test_average(self):
        calculator = Calculator()
        average = calculator.average([1])
        self.assertEqual(average, 1)
        
    def test_average_for_longer_lists(self):
        calculator = Calculator()
        average = calculator.average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print(calculator.print())
        self.assertEqual(average, 5.5)
        
    
  