

from src import CalculatorInterface

class MockCalculator(CalculatorInterface):
    def add(self, a, b):
        return print(f'I can add {a} and {b}')
    
    def average(self, numbers):
        return print(f'I can average {numbers}')
    
    def print(self):
        return print('I can print')
    