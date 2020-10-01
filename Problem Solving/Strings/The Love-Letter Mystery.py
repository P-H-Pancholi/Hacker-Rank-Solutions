#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    reductions = 0

    if len(s) % 2 != 0:
        half = s[:(len(s)//2)]
        other_half = s[(len(s)//2)+1:][-1::-1]
    else:
        half = s[:(len(s))//2]
        other_half = s[(len(s)+1)//2:][-1::-1]

    for i in range(len(half)):
        if half[i] != other_half[i]:
            reductions += abs(ord(half[i]) - ord(other_half[i]))

    return reductions


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(result)
