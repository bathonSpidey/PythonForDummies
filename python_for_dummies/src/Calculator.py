from src import CalculatorInterface


class Calculator(CalculatorInterface):
   def add(self, a, b):
      return a + b
   
   def average(self, numbers):
      return sum(numbers) / len(numbers)
   
   def print(self):
      array = [[1, 2, 3 ], 
               [4, 5, 6], 
               [8, 9, 10]]
      sub_array = array[:-3]
      print(array[0][1:])