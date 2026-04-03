

class BadInputException(Exception):
    """ Used when input is not the desired type """


class BadOperatorException(BadInputException):
    """ Used when operator is unknown """


class BadCharacterException(BadInputException):
    """ Used when input character is unknown """
    

class BadLogicException(Exception):
    """ 
    Used when logic is used the way it is not supposed to work 
    """


class UnknownCharacterException(Exception):
    """ 
    Used when the character we are working with is unknown / unexpected 
    """
    
