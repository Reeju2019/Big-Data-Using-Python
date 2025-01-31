"""
This module contains functions for basic mathematical operations including addition, subtraction, multiplication, and division.
"""

def add(a: float, b: float) -> float:
    """
    Adds two numbers.
    
    Args:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first number.
    
    Args:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        float: The difference between the two numbers.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.
    
    Args:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        float: The product of the two numbers.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second number.
    
    Args:
        a (float): The numerator.
        b (float): The denominator.
    
    Returns:
        float: The quotient of the two numbers.
    
    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b