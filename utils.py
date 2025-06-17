"""
utils.py

This module provides basic arithmetic operations: addition, subtraction,
multiplication, and division.
"""


def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtract one integer from another.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The result of a minus b.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The product of a and b.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Divide one integer by another.

    Args:
        a (int): Numerator.
        b (int): Denominator.

    Returns:
        float: The result of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b
