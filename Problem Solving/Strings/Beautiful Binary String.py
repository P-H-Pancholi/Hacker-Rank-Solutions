#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    count = 0
    b = list(b)
    for i in range(len(b)-2):
        #print("Checking for ", "".join(b[i:i+3]), " in string " , "".join(b) )
        if "".join(b[i:i+3]) == '010':
            b[i+2] = '1'
            count += 1
    return count

if __name__ == '__main__':

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    print(result)
