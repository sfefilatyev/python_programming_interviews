#/usr/bin/python

# How would you compute number of very large 64-bits word?
# Parity of a binary word is 1 if the number of 1s in the word is odd, otherwise parity is 0.
# For example, the parity of 1011 is 1, and the parity of 10001000 is 0.
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
