# Implement a function that takes an input string and returns true if the string is a palindromic string.
# For the purpose of this problem, a palindromic string is defined as a string which, if all non-alpha
# numberic characters are removed reads the same front to back igroning the case.

import sys

def is_palindromic_string(s):
    """Return true if the input string is a palindrome.

    All non-alpha-numeric charactres are ignored and so is the case.
    """
    return all([x == y for x, y in zip(map(str.lower, filter(str.isalnum, s)), map(str.lower, filter(str.isalnum, reversed(s))))])


if __name__ == "__main__":
    s = input("Please input a single string for palindromacity check:")
    print(is_palindromic_string(s))
