# UI elements
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon


# custom-defined UI elements
from ui.elements.display import Display
from ui.elements.buttons import Buttons


# to be used for type checking only
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from logic.operators import Operator
    

# utils from logic via connector
from connector import get_operator


class Calculator(QWidget):
    def __init__(self, app: QApplication) -> None:
        super().__init__()
        self.properties_setup()
        self.ui_setup()
        self.memory_setup()
        

    def properties_setup(self) -> None:
        """ 
        Setup window related properties for the calculator
        """
        
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("./ui/assets/icon.png"))
    

    def ui_setup(self) -> None:
        """ 
        Creates the main layout of the calculator using elements
        """
        
        # this is the app's default layout
        self.main_layout = QVBoxLayout()
        
        # Initialize the elements
        self.display = Display(calculator=self)
        self.buttons = Buttons(calculator=self)
                
        # set as the main layout of the calculator
        self.setLayout(self.main_layout)
        

    def memory_setup(self) -> None:
        """
        Attach variables to serve as the memory of the calculator.
        """
        self.operator: Operator = None
        self.num1: float = None
        self.num2: float = None
        

    """ ______________ Validation functions _____________"""
    

    def is_memory_valid_for_calculation(self) -> bool:
        """ 
        check if memory is valid for calculations 
        """
        
        return all([self.operator, self.num1]) is not None


    """ ______________ Utils to be used by buttons _______________ """
    

    def clear_memory(self) -> None:
        """
        Recalls memory setup for cleaning up memory
        """
        self.memory_setup()
        

    def clear_display(self) -> None:
        """
        Clears the display of the calculator
        """
        self.display.clear()
        

    def set_display_text(self, text: str | float) -> None:
        """
        Sets the given text on the display
        """
        self.display.setText(str(text))
        

    def add_display_text(self, text: str | float) -> None:
        """
        Adds any given text to the existing text on the screen
        """
        self.display.setText(self.display.text() + str(text))
        

    def set_num1_from_display(self) -> None:
        """
        Set num1 value of the calculator.
        """
        self.num1 = float(self.display.text())


    def set_num2_from_display(self) -> None:
        """
        Set num2 value of the calculator. When doing this we already
        would have the entire statement written on the display, so just
        to be careful
        """
        self.num2 = float(self.display.text())
        

    def set_operator(self, text: str) -> None:
        """
        Set the operator from the display, only usable when 
        """
        self.operator = get_operator(text)
        

    def operate(self) -> None:
        """
        Carry out the operation at hand
        """
        
        return self.operator.operate(self.num1, self.num2)

