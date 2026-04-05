# UI elements
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon


# custom-defined UI elements
from ui.elements.calculatorDisplay import CalculatorDisplay
from ui.elements.calculatorButtonGrid import CalculatorButtonGrid
    

# utils from logic via connector
from connector import Connector

# custom exceptions
from exceptions import BadExpressionException, BadLogicException


class Calculator(QWidget):
    """
    This class internally syncs the calculation memory with the 
    display memory.
    """
    
    def __init__(self, _: QApplication, debug: bool=False) -> None:
        super().__init__()
        self._properties_setup()
        self._ui_setup()
        self._variables_setup(debug)


    """ _________________ Public Functions __________________ """
        
        
    def operate(self) -> None:
        """
        Carry out the operation at hand
        """
        
        try:
            result = self.operator.operate(self.expression, self.debug)
            self._set_display(result)
            
        except BadExpressionException as e:
            self.expression.clear()
            self._set_display("ERR")
            print(e)
        

    def clear(self) -> None:
        """
        Clears the display of the calculator
        """
        
        self.expression.clear()
        self._set_display("")
        

    def backspace(self) -> str:
        """
        Removes one char from the display and internal expression.
        
        Returns:
            str: the removed character
        """
        
        removed_char = self.expression.backspace()
        text = self.expression.get_displayable()
        self._set_display(text)
        
        return removed_char
        

    def add(self, char: str) -> None:
        """
        Adds one char to the display and internal expression.
        """
        
        self.expression.add(char)
        text = self.expression.get_displayable()
        self._set_display(text)
        

    def display_decimal(self) -> None:
        """
        Converts the displayed expression to a decimal if possible. 
        
        Raises:
            BadLogicException: if the conversion is not possible
        """
        
        curr_display_text = self.expression.get_calculatable()
        
        try:
            self._set_display(str(float(self.operator.operate(curr_display_text))))
        except:
            raise BadLogicException("Cannot convert to decimal")
    

    """ ________________ Private Functions ________________ """
        

    def _properties_setup(self) -> None:
        """ 
        Setup window related properties for the calculator
        """
        
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("./ui/assets/icon.png"))
    

    def _ui_setup(self) -> None:
        """ 
        Creates the main layout of the calculator using elements
        """
        
        # this is the app's default layout
        self.main_layout = QVBoxLayout()
        
        # Initialize the elements
        self.display = CalculatorDisplay(calculator=self)
        self.buttons = CalculatorButtonGrid(calculator=self)
                
        # set as the main layout of the calculator
        self.setLayout(self.main_layout)
        

    def _variables_setup(self, debug: bool=False) -> None:
        """
        Attach variables to serve as the memory of the calculator.
        """
        
        self.operator = Connector.get_operator()
        self.expression = Connector.get_expression()
        self.debug = debug
    

    def _set_display(self, text: str | float | int) -> None:
        """
        Set the display text to the given text.
        """
        self.display.setText(text)
        
