#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):

    solution_matrix = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s2) + 1)]

    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):

            if s1[i-1] == s2[j-1]:
                solution_matrix[i][j] = solution_matrix[i-1][j-1] + 1
            else:
                solution_matrix[i][j] = max(solution_matrix[i-1][j], solution_matrix[i][j-1])

    for i in range(len(s1) + 1):
        print(solution_matrix[i])

    return solution_matrix[len(s1)][len(s2)]

if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)
