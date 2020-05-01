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
    result = ""

    while(True):
        if len(a) == 0 and len(b) == 0:
            break

        if len(a) == 0:
            result += "".join(b)
            break

        if len(b) == 0:
            result += "".join(a)
            break

        if a[0] > b[0]:
            result += b[0]
            b.pop(0)
            continue

        if b[0] > a[0]:
            result += a[0]
            a.pop(0)
            continue

        if a[0] == b[0]:
            if a[1:] > b[1:]:
                result += b[0]
                b.pop(0)
                continue
            else:
                result += a[0]
                a.pop(0)
                continue


    return result



if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        print(result)
