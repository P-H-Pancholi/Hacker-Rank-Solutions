#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):

    len_a = len(a)
    len_b = len(b)

    solution_matrix = [[False for _ in range(len_b + 1)] for _ in range(len_a+1)]

    solution_matrix[0][0] = True

    for i in range(len_a):
        print("Checking ", a[i])
        for j in range(len_b + 1):
            if a[i].islower():# We check if the char is lowercase case if yes then we can delete it then we remain in same state as previous.
                solution_matrix[i+1][j] = (solution_matrix[i+1][j] or solution_matrix[i][j])

            if j < len_b and a[i].upper() == b[j]:# But if the uppercase of the character is matching then we can select it and we move to next state.
                solution_matrix[i+1][j+1] = (solution_matrix[i+1][j+1] or solution_matrix[i][j])

            #print(solution_matrix)
    if solution_matrix[len_a][len_b]:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)
