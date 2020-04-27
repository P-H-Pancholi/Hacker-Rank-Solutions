#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left, insort_left


def findMedian(d,listD):
    return listD[d // 2] if d % 2 == 1 else ((listD[d // 2] + listD[d // 2 - 1]) / 2)



# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notice_sent = 0
    listD = sorted(expenditure[:d])
    if len(expenditure) > d:
        for i in range(d,n):
            if expenditure[i] >= 2*findMedian(d,listD): notice_sent += 1
            del listD[bisect_left(listD, expenditure[i-d])]
            insort_left(listD, expenditure[i])

    return notice_sent

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)
