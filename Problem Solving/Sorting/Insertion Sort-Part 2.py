
import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    shift = 0
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                shift += 1
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    print(shift)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
