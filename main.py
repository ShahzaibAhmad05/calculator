"""
Main file that handles the workflow. Invokes the ui
"""

# default imports
import sys
import os

# custom modules
from ui.calculator import Calculator

# pyqt stuff
from PyQt6.QtWidgets import QApplication


def main() -> None:
    # WARN the user on other platforms than windows
    if os.name != "nt" and input("This was supposed to run on windows and I mentioned it in the docs too.\nNote that I am not responsible for whatever UI comes next if you say yes.\n\nAre you still going to try and run it on this system? (y) ").strip().lower() not in ['yes', 'y']:
        sys.exit(0)
        
    app = QApplication(sys.argv)
    calculator = Calculator(app, debug=True)
    calculator.show()
    
    # connect the exit code of the app with system
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    
