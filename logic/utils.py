from logic.operators import Add, Subtract, Divide, Multiply, Operator
from exceptions import BadOperatorException


def decode_operator(operator: str) -> Operator:
    """
    Decoding the operator class type and returning a usable instance
    
    Args:
        operator: the operator input given by the user
    
    Returns:
        usable instance of the operator type decoded

    Raises:
        BadOperatorException: in case of unknown operator or bad input
    """
    
    if operator == "+":
        return Add()
    elif operator == "-":
        return Subtract()
    elif operator == "/":
        return Divide()
    elif operator == "*":
        return Multiply()
    else:
        raise BadOperatorException("Unknown operator, bad input.")
    
