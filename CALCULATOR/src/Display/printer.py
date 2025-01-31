"""
This module provides functions for displaying messages and interacting with the user.
"""

def show_menu() -> None:
    """
    Displays the calculator menu options.
    """
    print("""
    Calculator Menu:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    """)


def get_input(prompt: str) -> float:
    """
    Gets a floating-point number from the user based on a prompt.
    
    Args:
        prompt (str): The message to display when asking for input.
    
    Returns:
        float: The user's input as a float.
    """
    return float(input(prompt))


def show_result(result: float) -> None:
    """
    Displays the result of a mathematical operation.
    
    Args:
        result (float): The result to be displayed.
    """
    print(f"Result: {result}")