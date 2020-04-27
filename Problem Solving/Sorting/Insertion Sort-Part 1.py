import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    last = arr[n-1]
    i = n-1

    while arr[i-1] >= last and i > 0:
            arr[i] = arr[i-1]
            print(" ".join(map(str, arr)))
            i -= 1

    arr[i] = last
    print(" ".join(map(str, arr)))
    



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
