from abc import ABC, abstractmethod



class CalculatorInterface(ABC):
    @abstractmethod
    def add(self, a, b):
        pass
    
    @abstractmethod
    def average(self, numbers):
        pass
    
    @abstractmethod
    def print(self):
        pass