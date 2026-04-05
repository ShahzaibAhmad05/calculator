# Exception classes to be used here
from exceptions import UnknownCharacterException, BadLogicException


class Expression():
    """
    This static class helps decode the actual symbols of the buttons
    """
    
    def __init__(self) -> None:
        self._variables_setup()
        

    """ ___________________ Public functions _________________ """
    

    def add(self, char: str) -> None:
        """
        Adds a 'character' from a button to the expression. Decoding
        it beforehand.
        """
        
        try:
            self._add_to_calculatable_expression(char)
            self._add_to_display_expression(char)
        except UnknownCharacterException as e:
            print(e)
            

    def backspace(self) -> None:
        """
        Removes a 'character' from the end of the list.
        
        Raises:
            BadLogicException: when attempting to backspace an empty expression.
        """
        
        try:
            char_to_be_removed = self.calculatable_expression[-1]
            self.calculatable_expression = self.calculatable_expression[:-1]
            self.display_expression = self.display_expression[:-1]
            return char_to_be_removed
            
        except IndexError:
            raise BadLogicException("Cannot backspace an empty expression.")
            

    def clear(self) -> None:
        """
        Clears the expression completely.
        """
        self._variables_setup()
            

    def get_calculatable(self) -> str:
        """
        Used to fetch a calculatable piece of string of the expression.
        """
        return self._join_expression(self.calculatable_expression)
    

    def get_displayable(self) -> str:
        """
        Used to fetch a displayable piece of string of the expression.
        """
        return self._join_expression(self.display_expression)
        

    """ ________________ Private Functions ________________ """
        

    def _variables_setup(self) -> None:
        """
        Setups variables that are to be used by the memory.
        """
        
        self.calculatable_expression: list = []
        self.display_expression: list = []
        
        # characters valid to be added to the memory directly
        self.valid_chars: list = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '00',
            '-', '+', '.', '%', 
        ]
        
        # characters that need conversion and their converted versions
        self.calculatable_conversion: dict = {
            '×': '*', 
            '±': '-', 
            '𝑥²': '**2', 
            '√𝑥': 'sqrt(', 
            '÷': '/',
        }
        
        # characters that need conversion for display, or they have to be kept the same
        self.display_conversion: dict = {
            '×': '×', 
            '±': '-', 
            '𝑥²': '²', 
            '√𝑥': '√', 
            '÷': '÷',
        }
    

    def _add_to_calculatable_expression(self, char: str) -> None:
        """
        Adds the given character to the calculatable expression.
        
        Raises:
            UnknownCharacterException: when the given character is not allowed at all.
        """
        
        try:
            if char not in self.valid_chars:
                char = self.calculatable_conversion[char]
                
            self.calculatable_expression.append(char)
            
        except KeyError:
            raise UnknownCharacterException(f"Given character is not valid.\nCharacter: {char}")
            
    
        
    def _add_to_display_expression(self, char: str) -> None:
        """
        Adds the given character to the display expression.
        
        Raises:
            UnknownCharacterException: when the given character is not allowed at all.
        """

        try:
            if char not in self.valid_chars:
                char = self.display_conversion[char]
            
            self.display_expression.append(char)
        
        except KeyError:
            raise UnknownCharacterException(f"Given character is not valid.\nCharacter: {char}")
        

    def _join_expression(self, expression: list) -> str:
        """
        Joins the expression list into a single string using custom logic
        that joins only the digits with spaces.
        """
        
        joined_expression: str = ""
        last_char: str = ""

        for curr_char in expression:
            if curr_char.isdigit():
                joined_expression += curr_char
            else:
                joined_expression += " " + curr_char + " "
                
            last_char = curr_char
    
        return joined_expression
    
