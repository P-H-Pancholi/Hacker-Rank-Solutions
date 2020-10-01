#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr,n):
    print(arr)
    s_arr = sorted(arr)

    cnt = 0
    first = 0
    last = 0
    first_cmp = True

    for i in range(n):
        if arr[i] != s_arr[i] and first_cmp:
            cnt += 1
            first = i + 1
            first_cmp = False
        elif arr[i] != s_arr[i] and not first_cmp:
            cnt += 1
            last = i + 1
        else:
            continue


    if cnt == 0:
        print("yes")
    else:
        if cnt == 2:
            print("yes")
            print("swap", first, last)
        else:
            if abs(first - last) + 1 == cnt and arr[last - 1:first-2:-1] == s_arr[first-1:last]:
                print("yes")
                print("reverse", first, last)
            else:
                print("no")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split(' ')))

    almostSorted(arr,n)
