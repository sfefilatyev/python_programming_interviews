# Implement integer to string conversion function.

import sys

def convert_int_to_str(num):
    """Converts integer number to its string representation."""
    if num == 0:
        return '0'
    sign = -1 if num < 0 else 1
    if sign == -1:
        num *= -1
    str_list = []
    while (num):
        reminder = num % 10
        num = num // 10
        str_list.append(chr(ord('0') + reminder))
    if sign == -1:
        str_list.append('-')
    return ''.join(reversed(str_list))
    


if __name__ == '__main__':
    assert len(sys.argv) == 2, "Please provide a single argument - number"
    num_str = sys.argv[1]
    print("provided argument = {}".format(num_str))
    num = int(num_str)
    print("Converted to string: {}".format(convert_int_to_str(num)))
