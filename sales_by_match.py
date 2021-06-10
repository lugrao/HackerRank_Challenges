#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    socks = {}

    for sock in ar:
        if sock in socks:
            socks[sock] += 1
        else:
            socks[sock] = 1
        if socks[sock] == 2:
            socks[sock] = 0
            pairs += 1

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
