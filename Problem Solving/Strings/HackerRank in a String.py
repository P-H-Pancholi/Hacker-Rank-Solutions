#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    stk = [c for c in "knarrekcah"]
    for c in s:
        top = len(stk) - 1
        if c == stk[top]:
            stk.pop()
            if len(stk) == 0:
                print("YES")
                break
    print("NO")


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
