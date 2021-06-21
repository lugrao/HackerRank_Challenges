#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a_chars = defaultdict(int)
    deletions = 0
    
    for char in a:
        a_chars[char] += 1
            
    for char in b:
        if a_chars[char] > 0:
            a_chars[char] -= 1
        else:
            deletions += 1
    
    for char in a_chars:
        deletions += a_chars[char]
        
    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
