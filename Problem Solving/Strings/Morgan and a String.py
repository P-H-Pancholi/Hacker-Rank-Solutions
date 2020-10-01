#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the morganAndString function below.
def morganAndString(a, b):
    a = list(a)
    b = list(b)

    a.reverse()
    b.reverse()

    print(a,b)
    result = ""

    while(True):

        if len(a) == 0 and len(b) == 0:
            break

        if len(a) == 0:
            while len(b) > 0:
                result += b.pop()
            break

        if len(b) == 0:
            while len(a) > 0:
                result += a.pop()
            break
        print(a,b)

        print(a[-1],b[-1])


        if a[-1] > b[-1]:
            result += b.pop()
            continue

        if b[-1] > a[-1]:
            result += a.pop()
            continue

        if a[-1] == b[-1]:
            if a[-2::-1] > b[-2::-1]:
                result += b.pop()
                continue
            else:
                result += a.pop()
                continue


    return result



if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        print(result)
