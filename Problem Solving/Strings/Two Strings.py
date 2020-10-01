#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    result = 'NO'
    for c in set(s1):
        if c in set(s2):
            result = 'YES'
            break
    return result

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)
