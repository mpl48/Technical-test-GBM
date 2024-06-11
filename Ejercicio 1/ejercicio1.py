"""
palindrome_checker.py

This module provides a function to check if a given string is a palindrome.

Functions:
    es_palindromo(s: str) -> bool
        Returns True if the string `s` is a palindrome, otherwise False.
"""

def es_palindromo(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a string that reads the same forward and backward.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if `s` is a palindrome, False otherwise.
    """
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    print(es_palindromo("rap"))   # Output: False
    print(es_palindromo("radar")) # Output: True