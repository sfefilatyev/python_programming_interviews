#/usr/bin/python

# How would you compute number of very large 64-bits word?
import sys

def parity(x):
    parity_result = 0
    while x:
        if x & 1:
            parity_result += 1
        x >>= 1
    if parity_result % 2 == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    print(parity(int(sys.argv[1])))
