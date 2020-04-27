#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countSort(arr):
    for i,l in enumerate(arr):
        if i < len(arr)//2:
            l[1] = '-'
    sorted_list = [[] for _ in range(100)]
    for l in arr:
        sorted_list[int(l[0])].append(l)

    for l in sorted_list:
        for m in l:
            print(m[1], end = " ")

if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
