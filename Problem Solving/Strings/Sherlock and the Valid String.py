#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    s_s = list(set(s))
    cnt = [0 for _ in range(len(s_s))]



    print(s_s)

    for i in range(len(s_s)):
        cnt[i] = s.count(s_s[i])


    print(cnt)

    max_cnt = max(cnt)

    min_cnt = min(cnt)

    n_max_cnt = cnt.count(max_cnt)

    n_min_cnt = cnt.count(min_cnt)

    if max_cnt == min_cnt:
        return 'YES'

    if (n_max_cnt == 1 and n_min_cnt == len(cnt) - 1):
        if abs(max_cnt - min_cnt) == 1 or (max_cnt == 1):
            return 'YES'

    if (n_min_cnt == 1 and n_max_cnt == len(cnt) - 1):
        if abs(max_cnt - min_cnt) == 1 or (min_cnt == 1):
            return 'YES'


    return 'NO'



if __name__ == '__main__':


    s = input()

    result = isValid(s)

    print(result)
