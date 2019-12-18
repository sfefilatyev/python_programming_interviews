#/usr/bin/python

# Swap bits of large 64-bit number.
# Implement code that takes an input 64-bit integers and swaps bits at indices `i` and `j`

import sys

def generate_mask(i):
    number = 1 << i
    return number

def swap_bits(number, i, j):
    mask_i = 1 << i
    mask_j = 1 << j
    mask = mask_i | mask_j
    
    number = number ^ mask
    return number

if __name__ == "__main__":
    print("Swapped bits :")
    print(swap_bits(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
