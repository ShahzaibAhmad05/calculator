# pyqt6 stuff
from PyQt6.QtWidgets import QGridLayout

# custom styling
from ui.styling import Style


# buttons to put in this grid
from ui.elements.calculatorButton import (
    PrimaryCalculatorButton, 
    SecondaryCalculatorButton
)

# imported only during type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.calculator import Calculator


class CalculatorButtonGrid(QGridLayout):
    """
    Grid housing functional buttons on the calculator
    """
    
    def __init__(self, calculator: 'Calculator'):
        super().__init__()
        self.calculator = calculator
        self._buttons_setup()
        self._apply_style()
        calculator.main_layout.addLayout(self)
        

    """ ____________ Private Functions _____________ """
    

    def _apply_style(self) -> None:
        Style.calculator_button_grid(self)
    

    def _buttons_setup(self) -> None:
        self._primary_buttons_setup()
        self._secondary_buttons_setup()
    

    def _primary_buttons_setup(self) -> None:
        """
        Adds primary buttons.
        """
        
        primary_buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),  # there is a button missing at 5,0
        ]
            
        for text, row, col in primary_buttons:
            button = PrimaryCalculatorButton(text, self.calculator)
            self.addWidget(button, row, col)
        

    def _secondary_buttons_setup(self) -> None:
        """
        Adds secondary buttons.
        """
        
        secondary_buttons = [
            ('DEC', 0, 0), ('CE', 0, 1), ('C', 0, 2), ('⌫', 0, 3), 
            ('%', 1, 0), ('𝑥²', 1, 1), ('±', 1, 2), ('÷', 1, 3)
        ]

        for text, row, col in secondary_buttons:
            button = SecondaryCalculatorButton(text, self.calculator)
            self.addWidget(button, row, col)

