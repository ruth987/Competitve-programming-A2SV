#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    fre_array = []
    for i in range(100) :
        fre_array.append(0)
    for item in arr :
        for x in range (100):
            if x == item :
                fre_array[x] += 1
    return fre_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
