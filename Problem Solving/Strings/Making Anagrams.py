#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    count = 0
    ls1 = list(s1)
    ls2 = list(s2)
    for c in s1:
        if c not in ls2:
            count += 1
        else:
            ls2.remove(c)

    for c in s2:
        if c not in ls1:
            count += 1
        else:
            ls1.remove(c)

    return count

if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(result)
