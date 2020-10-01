#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the steadyGene function below.
def steadyGene(gene):
    min_len_str = len(gene)

    occurences = dict()
    occurences['A'] = 0
    occurences['C'] = 0
    occurences['T'] = 0
    occurences['G'] = 0

    expected = len(gene)//4

    for g in gene:
        occurences[g] += 1

    for x in occurences:
        occurences[x] = max(0, occurences[x] - expected)

    if occurences['A'] == 0 and occurences['C'] == 0 and occurences['T'] == 0 and occurences['G'] == 0:
        return 0

    found = dict()

    found['A'] = 0
    found['C'] = 0
    found['T'] = 0
    found['G'] = 0

    head = 0
    tail = 0

    while head != len(gene):
        found[gene[head]] += 1
        if found['A'] >= occurences['A'] and found['C'] >= occurences['C'] and found['T'] >= occurences['T'] and found['G'] >= occurences['G']:
            min_len_str = min(min_len_str, head-tail+1)

            while found[gene[tail]] > occurences[gene[tail]]:
                found[gene[tail]] -= 1
                tail += 1
                min_len_str = min(min_len_str, head-tail+1)

        head += 1

    return min_len_str


if __name__ == '__main__':

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    print(result)
