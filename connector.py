"""
This code connects the UI with logic, acting as a one-way bridge
for two kinds of connections:

- UI to UI
- UI to Logic
"""

# logic functions
from logic.operator import Operator
from logic.expression import Expression


# only for type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.calculator import Calculator
    from logic.operator import Operator


class Connector:
    
    @staticmethod
    def on_calculator_button_click(calculator: 'Calculator', text: str) -> None:
        """ 
        Invokes when a button is clicked. Requires the text of the button for action.
        """
        
        if text == "=":
            calculator.operate()
            
        elif text == "⌫":
            calculator.backspace()
            
        elif text == "±":
            char = calculator.backspace()
            calculator.add("-")
            calculator.add(char)
        
        elif text in ['C', 'CE']:
            calculator.clear()
            
        else:
            calculator.add(text)
    

    @staticmethod
    def get_operator() -> Operator:
        """
        Connector used to get an instance of the Operator class.
        """
        return Operator()


    @staticmethod
    def get_expression() -> Expression:
        """
        Connector used to get an instance of the Expression class.
        """
        return Expression()
        
