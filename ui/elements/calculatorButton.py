# pyqt stuff
from PyQt6.QtWidgets import QPushButton

# custom styling for buttons
from ui.styling import Style

# connector module for accessing logic module
from connector import Connector


# imports for type checking 
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.calculator import Calculator
    

class CalculatorButton(QPushButton):
    """
    Main CalculatorButton class housing common functions of buttons.
    """
    
    def __init__(self, text: str, calculator: 'Calculator'):
        super().__init__(text=text, parent=calculator)
        
        self.text_str = text
        self.calculator = calculator
        
        self._functionality_setup()
        self._apply_style()
        

    """ _________ Internal Functions __________ """
        

    def _functionality_setup(self) -> None:
        """
        Connect click behaviour with a function
        """
        self.clicked.connect(
            lambda _, x=self.calculator, y=self.text_str:
            Connector.on_calculator_button_click(x, y)
        )


    def _apply_style(self) -> None:
        """
        Apply style to the generic button class
        """
        Style.calculator_button(self)
    

class PrimaryCalculatorButton(CalculatorButton):
    """
    Main buttons of the calculator, includes numbers 1-9, etc.
    """
    
    def __init__(self, text: str, calculator: 'Calculator'):
        super().__init__(text, calculator)
        
        self.text_str = text
        self.calculator = calculator
        
        self._apply_style()
        

    def _apply_style(self) -> None:
        """
        Apply style to the Primary button
        """
        
        super()._apply_style()
        Style.primary_calculator_button(self)


class SecondaryCalculatorButton(CalculatorButton):
    """
    Secondary buttons of the calculator, includes the buttons on the
    top-most row and right-most column.
    """
    
    def __init__(self, text: str, calculator: 'Calculator'):
        super().__init__(text, calculator)
        
        self.text_str = text
        self.calculator = calculator
        
        self._apply_style()
        

    def _apply_style(self) -> None:
        """
        Apply style to the Secondary button
        """
        
        super()._apply_style()
        Style.secondary_calculator_button(self)

