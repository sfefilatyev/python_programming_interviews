# Implement string to integer conversion function. 
# For example, if the input to the function is "314" it should output 314. 
# Should handle negative numbers.

import sys
import string

def str_to_int_conversion(str_num):
    """Convert string representation of an integer to that int without use of 'int' function."""
    start_index = 0
    if str_num[0] == '-':
        sign = -1
        start_index = 1
    else:
        start_index = 0
        sign = 1

    partial_num = 0

    for i in range(start_index, len(str_num)):
        partial_num = partial_num * 10 + string.digits.index(str_num[i])

    partial_num *= sign

    return partial_num


if __name__ == '__main__':
    assert len(sys.argv) == 2, "Please provide a single integer argument"
    str_num = sys.argv[1]

    print("Obtained string = {}".format(str_num))

    print("Converted int = {}".format(str_to_int_conversion(str_num)))

        
