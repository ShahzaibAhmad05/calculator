# pyqt stuff
from PyQt6.QtGui import QFont


# for type checking only
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.elements.calculatorButtonGrid import CalculatorButtonGrid
    from ui.elements.calculatorButton import (
        PrimaryCalculatorButton, 
        SecondaryCalculatorButton, 
        CalculatorButton
    )
    from ui.elements.calculatorDisplay import CalculatorDisplay


class Style:
    
    @staticmethod
    def calculator_button_grid(grid: 'CalculatorButtonGrid') -> None:
        """
        Styling for CalculatorButtonGrid
        """
        grid.setSpacing(0)
        

    @staticmethod
    def calculator_button(button: 'CalculatorButton') -> None:
        """
        Styles the generic button class
        """
        button.setFixedHeight(50)
        button.setFixedWidth(75)
        
    
    @staticmethod
    def primary_calculator_button(button: 'PrimaryCalculatorButton') -> None:
        """
        Styles buttons for the calculator.
        """ 
        button.setFont(Style._get_font(font_size=14))
        button.setStyleSheet(button.styleSheet() + """
            QPushButton {
                background-color: rgb(59, 59, 59);
            }
                             
            QPushButton:hover {
                background-color: rgb(48, 48, 48);
            }
        """)
        
    
    @staticmethod
    def secondary_calculator_button(button: 'SecondaryCalculatorButton') -> None:
        """
        Styles buttons for the calculator.
        """
        button.setFont(Style._get_font(font_size=12))
        button.setStyleSheet(button.styleSheet() + """
            QPushButton {
                background-color: rgb(48, 48, 48);
            }
                             
            QPushButton:hover {
                background-color: rgb(59, 59, 59);
            }
        """)
        

    @staticmethod
    def calculator_display(display: 'CalculatorDisplay') -> None:
        display.setMinimumHeight(50)
        display.setFont(Style._get_font(font_size=14))
        display.setReadOnly(True)
        
        display.setStyleSheet("""
            QLineEdit {
                padding: 20px 6px;
                background-color: rgb(30, 30, 30);
                border-radius: 5px;
            }
                                
            QLineEdit::active {
                background-color: rgb(30, 30, 30);
            }
        """)
        

    """ _____________ Helper Utils for styling ____________ """


    def _get_font(font_size: int) -> QFont:
        font = QFont()
        font.setPointSize(font_size)
        return font

