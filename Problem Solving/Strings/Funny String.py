#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    str1_l = [ord(c) for c in s]
    str1_rev_l = [ord(c) for c in s[-1::-1]]

    str1_diff = [abs(str1_l[i]-str1_l[i+1]) for i in range(len(s) - 1)]
    str1_rev_diff = [abs(str1_rev_l[i]-str1_rev_l[i+1]) for i in range(len(s) - 1)]
    print(str1_diff, "  ",str1_rev_diff)
    funny = "Funny"
    for i in range(len(str1_diff)):
        if str1_diff[i] != str1_rev_diff[i]:
            funny = "Not Funny"
    return funny



if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
