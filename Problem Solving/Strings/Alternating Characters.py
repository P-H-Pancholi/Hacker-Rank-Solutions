#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0
    l_a = s.split('b')
    l_b = s.split('a')
    for str in l_a:
        if len(str) > 1:
            deletions += len(str)-1
    for str in l_b:
        if len(str) > 1:
            deletions += len(str)-1

    return deletions



if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)
