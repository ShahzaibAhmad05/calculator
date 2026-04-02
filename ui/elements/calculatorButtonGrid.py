# pyqt6 stuff
from PyQt6.QtWidgets import QPushButton, QGridLayout

# custom styling
from ui.styling import Style

# logic connector
from connector import Connector

# buttons to put in this grid
from ui.elements.calculatorButton import primaryCalculatorButton, secondaryCalculatorButton


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
        
        self._primary_buttons_setup()
        self._secondary_buttons_setup()
        Style.calculator_button_grid(self)
        calculator.main_layout.addLayout(self)
        

    """ ____________ Internal Functions _____________ """
    

    def _primary_buttons_setup(self) -> None:
        """
        Adds primary buttons.
        """
        
        primary_buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('x', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('÷', 4, 2), ('=', 4, 3),
        ]
            
        for text, row, col in primary_buttons:
            button = secondaryCalculatorButton(self.calculator, text=text)
            self.addWidget(button, row, col)
        

    def _secondary_buttons_setup(self) -> None:
        """
        Adds secondary buttons.
        """
        
        secondary_buttons = [
            ('%', 0, 0), ('CE', 0, 1), ('C', 0, 2), ('⌫', 0, 3),
        ]

        for text, row, col in secondary_buttons:
            button = primaryCalculatorButton(self.calculator, text=text)
            self.addWidget(button, row, col)

