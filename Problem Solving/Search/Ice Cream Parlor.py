#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):

    idx = 0
    idy = 0

    for i,price1 in enumerate(arr):
        for j,price2 in enumerate(arr):
            if i != j and price1 + price2 == m:
                idx = i + 1
                idy = j + 1

    if idx > idy:
        return [idy ,idx]
    else:
        return [idx ,idy]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
