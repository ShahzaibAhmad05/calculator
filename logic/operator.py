"""
Main logic file for basic calculation operations, works 
only with float values.
"""

# for expression calculation
from sympy import sympify


# for type checking only
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from logic.expression import Expression


class Operator:
    """
    Simple single function operator. Pass the expression to the operate function
    and calculate the result any time.
    """ 
    
    def __init__(self):
        pass
    
    
    def operate(self, expression: 'Expression') -> str:
        """
        Returns the string of the solved expression. Might be a 
        fraction, but it is guaranteed to be float convertible.
        """
        return sympify(expression.get_calculatable())
    
