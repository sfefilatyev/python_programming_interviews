# Write a program which takes as input an array of digits encoding a non-negative decimal integer D
# and updates the array to represent the integer D+1. For example, if the input  is <1, 2, 9> then
# you should update the array to <1, 3, 0>

import sys

def increment_integer(integer):
    """Incorement an arbitrary precision integer represented by array.

       Args:
            integer(list): integer number represented by a list of integers.
    """
    # Reversing for the ease of pro
    integer.reverse()
    carry = 0
    index = 0
    while index < len(integer):
        digit = integer[index]
        if index == 0:
            digit += 1
        else:
            digit = digit + carry

        if digit >= 10:
            digit = digit % 10
            carry = 1
        else:
            carry = 0
        integer[index] = digit
        index += 1

    if carry != 0:
        integer.append(1)
    integer.reverse()
    integer = [str(x) for x in integer]
    integer = "".join(integer)
    return integer


if __name__ == "__main__":
    integer = sys.argv[1]  # of type 'str'
    print("Obtained number: {}".format(sys.argv[1]))
    integer = list(integer)  # of type 'list'
    integer = [int(x) for x in integer]  # of type List[int]
    print("Incremented number: {}".format(increment_integer(integer)))
