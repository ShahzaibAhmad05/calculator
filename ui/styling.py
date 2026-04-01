# pyqt stuff
from PyQt6.QtWidgets import QPushButton, QLineEdit
from PyQt6.QtGui import QFont


def style_button(button: QPushButton) -> QPushButton:
    button.setMinimumSize(75, 75)
    button.setFont(get_font(font_size=20))
    return button


def style_display(line_edit: QLineEdit) -> QLineEdit:
    line_edit.setMinimumHeight(75)
    line_edit.setFont(get_font(font_size=20))
    
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


def get_font(font_size: int) -> QFont:
    font = QFont()
    font.setPointSize(font_size)
    font.setBold(True)
    return font

