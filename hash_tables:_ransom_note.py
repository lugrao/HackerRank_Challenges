#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    magazine_words = {}
    word_count = len(note)

    for word in magazine:
        if word in magazine_words:
            magazine_words[word] += 1
        else:
            magazine_words[word] = 1

    for word in note:
        if word in magazine_words:
            if magazine_words[word] == 0:
                return print("No")
            magazine_words[word] -= 1
            word_count -= 1

    if word_count == 0:
        return print("Yes")
    return print("No")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
