# Reverse all words in a sentense.

import sys

def reverse_all_words(s):
    """Reverse all words in an input string-stentense."""
    def reverse_range(string, start, finish):
        while start < finish:
            string[start], string[finish] = string[finish], string[start]
            start += 1
            finish -= 1

    reverse_range(s, 0, len(s) - 1) 

    start = 0
    while(True):
        finish = start
        while finish < len(s) and s[finish] != ' ':
            finish += 1
        if finish == len(s):
            break
        if start != finish:
            reverse_range(s, start, finish - 1)
        start = finish + 1

    reverse_range(s, start, finish -1)
    return s


if __name__ == '__main__':
    string = input("Input a sentense: ")
    string = list(string)
    string = reverse_all_words(string)
    string = "".join(string)
    print(string)
