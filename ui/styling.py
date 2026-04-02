# pyqt stuff
from PyQt6.QtWidgets import QPushButton, QLineEdit, QGridLayout
from PyQt6.QtGui import QFont


# for type checking only
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.elements.calculatorButtonGrid import CalculatorButtonGrid, CalculatorButton
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
        Styles buttons for the calculator.
        """
        button.setFixedSize(50, 50)   
        button.setFont(Style._get_font(font_size=14))


    @staticmethod
    def calculator_display(display: 'CalculatorDisplay') -> QLineEdit:
        display.setMinimumHeight(50)
        display.setFont(Style._get_font(font_size=14))
        display.setReadOnly(True)
        
        display.setStyleSheet("""
            QLineEdit {
                padding-left: 6px;
                padding-right: 6px;
                background-color: rgb(43, 43, 43);
                border: 1px solid rgb(53, 53, 53);
                border-radius: 5px;
            }
                                
            QLineEdit::active {
                background-color: rgb(43, 43, 43);
                border: 1px solid rgb(53, 53, 53);
            }
        """)
        

    """ _____________ Helper Utils for styling ____________ """


    def _get_font(font_size: int) -> QFont:
        font = QFont()
        font.setPointSize(font_size)
        font.setBold(True)
        return font

