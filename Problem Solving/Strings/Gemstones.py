#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    minerals = list("abcdefghijklmnopqrstuvwxyz")
    gemstones = 0
    for mineral in minerals:
        if all( (mineral in  ore) for ore in arr ):
            gemstones += 1
    return gemstones



if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)
    print(result)
