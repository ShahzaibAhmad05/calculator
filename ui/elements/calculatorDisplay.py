# pyqt6 stuff
from PyQt6.QtWidgets import QLineEdit

# custom styling
from ui.styling import Style


# imports only during type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.calculator import Calculator


class CalculatorDisplay(QLineEdit):
    
    def __init__(self, calculator: 'Calculator') -> None:
        super().__init__(parent=calculator)
        
        # style and add to layout of the calculator
        Style.calculator_display(self)
        calculator.main_layout.addWidget(self)
        

    def setText(self, a0: str | float | int):
        """
        Adds type conversion property to setText function
        """
        super().setText(str(a0))
        
