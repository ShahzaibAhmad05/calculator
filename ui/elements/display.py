# pyqt6 stuff
from PyQt6.QtWidgets import QLineEdit

# custom styling
from ui.styling import style_display


# imports only during type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.calculator import Calculator


class Display(QLineEdit):
    
    def __init__(self, calculator: 'Calculator') -> None:
        super().__init__(parent=calculator)
        
        # style and add to layout of the calculator
        style_display(self)
        calculator.main_layout.addWidget(self)
        
