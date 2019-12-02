#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getOneBits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def getOneBits(n):
    tmp = []
    count = 0
    while (not n/2 <= 0):
        val = n % 2
        n = n//2
        count = count +1
        if val == 1:
            tmp.append(count)
    result = []
    for v in tmp:
        result.append((count+1) -v)
    result.append(len(tmp))

    return result[::-1]

    # Write your code here
if __name__ == '__main__':
    pass