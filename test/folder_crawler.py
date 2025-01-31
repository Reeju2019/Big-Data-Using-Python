"""
os module provides a way of using operating system dependent functionality.
"""
import os


def list_files(startpath: str) -> None:
    """
    Prints the directory tree structure starting from the given path.

    Args:
        startpath (str): The root directory from which to start listing files.
    """
    for root, dirs, files in os.walk(startpath):
        level: int = root.replace(startpath, "").count(os.sep)
        indent: str = " " * 4 * (level)
        print("{}{}/".format(indent, os.path.basename(root)))
        subindent: str = " " * 4 * (level + 1)
        for f in files:
            print("{}{}".format(subindent, f))
            


list_files("./")
