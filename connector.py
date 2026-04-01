"""
This code connects the UI with logic
"""

# logic functions
from logic.utils import decode_operator


# only for type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.calculator import Calculator
    from logic.operators import Operator
    

def on_button_click(calculator: 'Calculator', text: str) -> None:
    """ 
    Invokes when a button is clicked. Requires the text of the button for action
    """
    
    if text == "C":
        calculator.clear_display()
        calculator.clear_memory()
        
        
    elif text in ["+", "-", "/", "*"]:
        # pick num1 and add spaces and operator
        calculator.set_num1_from_display()
        calculator.clear_display()
        calculator.set_operator(text)
        
        
    elif text == "=" and calculator.is_memory_valid_for_calculation():
        calculator.set_num2_from_display()
        
        result = calculator.operate()
        if result == int(result): result = int(result)
        
        calculator.set_display_text(result)
        
        
    else:   # in this case it is just a number
        calculator.add_display_text(text)
        

def get_operator(text: str) -> 'Operator':
    """
    Decode a given string of text and return the Operator
    """
    return decode_operator(text)

