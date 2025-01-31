""" Count the number of occurrences of a substring in a string. """
def count_substring(string: str, substring: str) -> int:
    """
    This function counts the number of occurrences of a substring in a string.
    
    Args:
        string (str): The string to search.
        substring (str): The substring to search for.

    Returns:
        int: The number of occurrences of the substring in the string.
    """
    count: int = 0
    n: int = len(string)
    m: int = len(substring)

    # Loop through the string
    for i in range(n - m + 1):  # Ensure we don't go out of bounds
        match: bool = True
        # Check if substring matches
        for j in range(m):
            if string[i + j] != substring[j]:
                match = False
                break
        if match:
            count += 1
    return count

# Example usage
in_string: str = "abcarabababcarcar"
in_substring: str = "car"
print("Occurrences:", count_substring(in_string, in_substring))
