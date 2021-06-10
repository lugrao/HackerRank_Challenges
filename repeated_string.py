#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a1, a2 = 0, 0
    mod = n % len(s)

    for i in range(len(s)):
        if s[i] == 'a':
            a1 += 1
            if i < mod:
                a2 += 1

    return int((n - (mod)) / len(s)) * a1 + a2

    # Another option that works with small n:
    # while s_len < n:
    #     for i in s:
    #         if i == 'a':
    #             a += 1
    #         s_len += 1
    #         if s_len == n:
    #             break
    # return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
