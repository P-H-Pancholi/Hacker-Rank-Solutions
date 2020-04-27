#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr = sorted(arr)
    min_diff = sys.maxsize
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j] - arr[i] < min_diff:
                result = []
                min_diff = arr[j] - arr[i]
                result.append(str(arr[i]))
                result.append(str(arr[j]))
                count = 1
            elif arr[j] - arr[i] == min_diff :
                count += 1
                result.append(str(arr[i]))
                result.append(str(arr[j]))
            else:
                continue
    return result




if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(" ".join(result))
