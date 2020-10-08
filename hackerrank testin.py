#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr=[0]*n
    # for i in range(n):
    #     arr.append(int(0))
    # print("arr ",arr)
    # print((queries))
    for i in queries:
        for j in range(i[0],i[1]+1):
            print(j)
            arr[j-1]=arr[j-1]+i[2]
    return max(arr)
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

