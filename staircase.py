#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n, hashes=1):
    print(" " * (n - hashes) + "#" * hashes)

    if hashes == n:
        return
    return staircase(n, hashes + 1)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
