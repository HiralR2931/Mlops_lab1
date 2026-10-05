def add(x, y):
    """
    Adds two numbers together.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y


def subtract(x, y):
    """
    Subtracts two numbers.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y


def multiply(x, y):
    """
    Multiplies two numbers together.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y


def power(x, y):
    """
    Custom: Raises x to the power of y.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x ** y


def modulo(x, y):
    """
    Custom: Returns remainder of x divided by y.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x % y


def compound_operation(x, y, z):
    """
    Custom: Performs (x + y) * z
    """
    return multiply(add(x, y), z)
