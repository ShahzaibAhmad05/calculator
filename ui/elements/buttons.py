# pyqt6 stuff
from PyQt6.QtWidgets import QPushButton, QGridLayout

# custom styling
from ui.styling import style_button

# logic connector
from connector import on_button_click


# imported only during type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.calculator import Calculator


class Buttons(QGridLayout):
    
    def __init__(self, calculator: 'Calculator'):
        super().__init__()
        self.calculator = calculator
        

        # define the buttons and add to the grid
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]
        

        for text, row, col in buttons:
            button = QPushButton(text=text)
            style_button(button)
            
            button.clicked.connect(
                lambda checked, 
                calculator=self.calculator,
                text=text: on_button_click(calculator, text)
            )
            
            self.addWidget(button, row, col)
            

        # add this layout class to the main layout
        calculator.main_layout.addLayout(self)
        
