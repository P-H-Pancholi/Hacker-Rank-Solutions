     #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def count_swaps(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]

    arrpos.sort(key = lambda it:it[1])

    vis = {k:False for k in range(n)}
    ans = 0
    for i in range(n):

        while True:
            if vis[i] or arrpos[i][0] == i:
                break
            else:
                ans += 1
                swapped_i = arrpos[i][0]
                arrpos[i], arrpos[swapped_i] = arrpos[swapped_i], arrpos[i]
    return ans

def lilysHomework(arr):
    return min(count_swaps(arr),count_swaps(arr[::-1]))

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    print(result)
