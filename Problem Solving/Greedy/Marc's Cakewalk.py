#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie = sorted(calorie, reverse = True)
    result = 0
    for j in range(len(calorie)):
        result += 2**j * calorie[j]

    return result

if __name__ == '__main__':

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)
