"""
    Write a function that takes a dictionary as an argument and returns a list of keys
"""

def dict_to_list(a: dict) -> list:
    """
    Write a function that takes a dictionary as an argument and returns a list of keys
    Args:
        a (dict): _description_

    Returns:
        list: _description_
    """
    return [*a]


print(dict_to_list({'a': 1, 'b': 2, 'c': 3}))  # ['a', 'b', 'c']