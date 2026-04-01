

class BadInputException(Exception):
    """ Used when input is not the desired type """
    pass


class BadOperatorException(BadInputException):
    """ Used when operator is unknown """
    pass

