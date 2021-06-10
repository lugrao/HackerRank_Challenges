#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hg_sum = None

    for i in range(1, 5):
        for j in range(1, 5):
            current_sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            current_sum += arr[i][j]
            current_sum += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]

            if hg_sum == None:
                hg_sum = current_sum
            elif current_sum > hg_sum:
                hg_sum = current_sum

    return hg_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
