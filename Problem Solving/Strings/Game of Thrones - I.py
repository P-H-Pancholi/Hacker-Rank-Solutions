#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    palindrome = 'NO'
    odd = 0
    set_s = set(s)

    for c in set_s:
        if s.count(c) % 2 != 0:
            count += 1

    if count <= 1:
        palindrome = 'YES'

    return palindrome




if __name__ == '__main__':

    s = input()

    result = gameOfThrones(s)

    print(result)
