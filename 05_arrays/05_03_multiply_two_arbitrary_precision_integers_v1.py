# Write a program that takes two arrays representing integers, and returns an integer representing their product.
# For example, since 193707721 x -761838257287 = -147573952589676412927, if the inputs are <1, 9, 3, 7, 0, 7, 7, 1> 
# and <-7, 6, 1, 8, 3, 8, 2, 8, 7>, your function should return the following array: 
# <-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7>.

import sys

def multiply_integer_arrays(num1, num2):
    "Multiply two integer array and return their product as third array."
    sign = -1 if (num1[0] ^ num2[0] < 0) else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    # the most length for the result is n + m where n=len(num1) and m=len(num2)
    num3 = [0 for _ in range(len(num1) + len(num2))]

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            num3[i + j + 1] += num1[i] * num2[j]
            num3[i + j] += num3[i + j+ 1] // 10
            num3[i + j + 1] = num3[i + j + 1] % 10

    # removing leading zeros
    while (num3[0] == 0):
        num3 = num3[1:]

    # setting the sign
    num3[0] *= sign

    return num3


if __name__ == '__main__':
    assert len(sys.argv) == 3, "Please provide two input integers"
    num1 = sys.argv[1]
    print("Num1 = {}".format(num1))
    num2 = sys.argv[2]
    print("Num2 = {}".format(num2))

    if num1[0] == '-':
        num1 = num1[1:]
        num1 = [int(x) for x in num1]
        num1[0] = -num1[0]
    else:
        num1 = [int(x) for x in num1]

    if num2[0] == '-':
        num2 = num2[1:]
        num2 = [int(x) for x in num2]
        num2[0] = -num2[0]
    else:
        num2 = [int(x) for x in num2]

    num3 = multiply_integer_arrays(num1, num2)
    print("Product = {}".format(str(num3)))
