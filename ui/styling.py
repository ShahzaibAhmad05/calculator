# pyqt stuff
from PyQt6.QtWidgets import QPushButton, QLineEdit
from PyQt6.QtGui import QFont


class Style:
    
    @staticmethod
    def calculatorButton(button: QPushButton) -> QPushButton:
        """
        Styles buttons for the calculator.
        """
        button.setFixedSize(50, 50)      
        button.setFont(Style._get_font(font_size=14))
        return button


    @staticmethod
    def calculatorDisplay(line_edit: QLineEdit) -> QLineEdit:
        line_edit.setMinimumHeight(50)
        line_edit.setFont(Style._get_font(font_size=14))
        
        line_edit.setStyleSheet("""
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
        
        line_edit.setReadOnly(True)
        return line_edit
        

    """ _____________ Helper Utils for styling ____________ """


    def _get_font(font_size: int) -> QFont:
        font = QFont()
        font.setPointSize(font_size)
        font.setBold(True)
        return font

