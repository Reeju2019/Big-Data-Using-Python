# d: dict[str, int] = {"a": 2.5, "b": 3}
'''
A module for ....
'''

# x: int = "6"

y: float = 3.5

name: str = "John"

x_list: list[int | str] = [1, 2, 3, "r"]

x_dict: dict[str, int] = {"a": 2, "b": 3}

def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

print(add_numbers(2, 3))

def string_cap(s: str) -> str | None:
    """
    Capitalizes the given string.

    Args:
        s (str): The string to capitalize.

    Returns:
        str: The capitalized string.
    """
    if s[0] == "h":
        return s.capitalize()
    
    return None

print(string_cap("hello"))
