#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    k = 5 * ((2*n)%3)
    if k > n:
        return -1
    else:
        return '5' * (n-k) + '3' * k

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))
