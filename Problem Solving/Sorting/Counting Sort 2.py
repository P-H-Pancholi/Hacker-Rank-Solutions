#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    count_list = [arr.count(i) for i in range(100)]
    sorted_list = []
    for i,count in enumerate(count_list):
        if count != 0:
            for _ in range(count):
                sorted_list.append(str(i))
    return sorted_list
if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(" ".join(result))
