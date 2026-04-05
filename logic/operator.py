"""
Main logic file for basic calculation operations, works 
only with float values.
"""

# for expression calculation
from sympy import sympify
from sympy.core.sympify import SympifyError


# exception types
from exceptions import BadExpressionException


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
    
    
    def operate(self, expression: 'Expression', debug: bool=False) -> str:
        """
        Returns the string of the solved expression. Might be a 
        fraction, but it is guaranteed to be float convertible.
        """
        
        try:
            calculatable_str = expression.get_calculatable()
            if debug:
                print(f"Expression to operate on: '{calculatable_str}'")
            return sympify(calculatable_str)
        
        except SympifyError:
            raise BadExpressionException(
                f"Bad expression. Cannot parse.\nExpression: '{calculatable_str}'")
    
