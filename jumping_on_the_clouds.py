#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, s=0):
    if len(c) == 1:
        return s
    if len(c) > 2:
        if c[2] == 0:
            return jumpingOnClouds(c[2:], s + 1)
    if c[1] == 0:
        return jumpingOnClouds(c[1:], s + 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
