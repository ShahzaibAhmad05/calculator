"""
Main file that handles the workflow. Invokes the ui
"""

import sys
from ui.calculator import Calculator
from PyQt6.QtWidgets import QApplication


def main() -> None:
    app = QApplication(sys.argv)
    calculator = Calculator(app)
    calculator.show()
    
    # connect the exit code of the app with system
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    
