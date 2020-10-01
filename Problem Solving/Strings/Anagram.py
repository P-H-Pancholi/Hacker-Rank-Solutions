#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 != 0:
        return -1

    half = list(s[:(len(s))//2])
    other_half = list(s[(len(s)+1)//2:])

    for i in range(len(half)):
        if half[i] in other_half:
            other_half.remove(half[i])
    return len(other_half)

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)
