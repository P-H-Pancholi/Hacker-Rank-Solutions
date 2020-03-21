#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    total_health_list = []

    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        genes_in_d = [d[i: j] for i in range(len(d)) for j in range(i + 1, len(d) + 1)]

        #print(genes_in_d)



        total_health = 0
        for gene1 in genes_in_d:
            #print("Checking for ",gene1, " in ")
            for i,gene2 in enumerate(genes[first:last+1]):
                #print("Checking with ", gene2)
                if gene1 == gene2:
                    #print("adding " , health[i+1])
                    total_health += health[i+1]
        total_health_list.append(total_health)


    print( min(total_health_list),max(total_health_list), sep = " ")
