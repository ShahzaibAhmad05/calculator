# pyqt stuff
from PyQt6.QtWidgets import QPushButton, QLineEdit
from PyQt6.QtGui import QFont


class Style:
    
    @staticmethod
    def calculatorButton(button: QPushButton) -> QPushButton:
        """
        Styles buttons for the calculator.
        """
        button.setMinimumWidth(75)      # height would follow since it is forced 1:1
        button.setFont(Style._get_font(font_size=20))
        return button


    @staticmethod
    def calculatorDisplay(line_edit: QLineEdit) -> QLineEdit:
        line_edit.setMinimumHeight(75)
        line_edit.setFont(Style._get_font(font_size=20))
        
        line_edit.setStyleSheet("""
            QLineEdit {
                padding-left: 12px;
                padding-right: 12px;
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

