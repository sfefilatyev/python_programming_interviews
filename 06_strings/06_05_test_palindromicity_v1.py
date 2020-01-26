# Implement a function that takes an input string and returns true if the string is a palindromic string.
# For the purpose of this problem, a palindromic string is defined as a string which, if all non-alpha
# numberic characters are removed reads the same front to back igroning the case.

import sys

def is_palindromic_string(s):
    """Return true if the input string is a palindrome.

    All non-alpha-numeric charactres are ignored and so is the case.
    """
    i = 0 # index for the beginning iterator.
    j = len(s) -1 # index for the end iterator.

    while (i < j):
        while (not s[i].isalnum() and i < j):
            i += 1
        while (not s[j].isalnum() and i < j):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1

    return True


if __name__ == "__main__":
    s = input("Please input a single string for palindromacity check:")
    print(is_palindromic_string(s))
