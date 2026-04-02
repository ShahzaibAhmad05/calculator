# pyqt6 stuff
from PyQt6.QtWidgets import QPushButton, QGridLayout

# custom styling
from ui.styling import Style

# logic connector
from connector import Connector


# imported only during type checking
from typing import TYPE_CHECKING, override
if TYPE_CHECKING:
    from ui.calculator import Calculator


class CalculatorButtonGrid(QGridLayout):
    
    def __init__(self, calculator: 'Calculator'):
        super().__init__()
        
        self.calculator = calculator
        self.buttons_setup()
        calculator.main_layout.addLayout(self)
        

    def buttons_setup(self) -> None:
        """
        defines and adds buttons to the grid.
        """
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for text, row, col in buttons:
            button = CalculatorButton(self.calculator, text=text)
            self.addWidget(button, row, col)
        
        
    def heightForWidth(self, width: int) -> int:
        """ 
        keeps 1:1 ratio between height and width. 
        """
        return width


class CalculatorButton(QPushButton):
    """ 
    Self resizing button. In case of styling, change the width only. The height will
    follow, maintaining a 1:1
    """
    
    def __init__(self, calculator: 'Calculator', text: str) -> None:
        super().__init__(text=text)
        Style.calculatorButton(self)
        
        self.clicked.connect(
            lambda _, 
            calculator=calculator,
            text=text: Connector.on_calculator_button_click(calculator, text)
        )
        
