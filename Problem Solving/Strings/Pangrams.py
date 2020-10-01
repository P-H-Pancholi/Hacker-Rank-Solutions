#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    result = "not panagram"
    stk = list("abcdefghijklmnopqrstuvwxyz")
    for c in s:
        if c.lower() in stk:
            stk.remove(c.lower())
        if len(stk) == 0:
            result = "panagram"
            break
    return result


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)
