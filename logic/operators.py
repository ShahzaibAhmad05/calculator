"""
Main logic file for basic calculation operations, works 
only with float values.
"""

from abc import abstractmethod


class Operator:
    @abstractmethod
    def operate(self, num1: float, num2: float) -> float:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Add(Operator):
    def operate(self, num1: float, num2: float) -> float:
        return num1 + num2
    
    def __str__(self):
        return "Addition"


class Subtract(Operator):
    def operate(self, num1: float, num2: float) -> float:
        return num1 - num2
    
    def __str__(self):
        return "Subtraction"


class Divide(Operator):
    def operate(self, num1: float, num2: float) -> float:
        return num1 / num2
    
    def __str__(self):
        return "Division"


class Multiply(Operator):
    def operate(self, num1: float, num2: float) -> float:
        return num1 * num2
    
    def __str__(self):
        return "Multiplication"
    
