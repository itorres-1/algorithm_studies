# link: https://www.hackerrank.com/challenges/non-divisible-subset/problem

import math
import os
import random
import re
import sys

from utils.combinatorics import getCombinations

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(divisor, int_set):
    def isDivisibile(divisor,int_set):
        for i,addend1 in enumerate(int_set):
            for addend2 in int_set[i+1:]:
                if (addend1+addend2) % divisor == 0: return True
        return False
    for m in range(len(int_set),0,-1):
        all_subsets = getCombinations(collection=int_set,m = m, repetition=False)
        for subset in all_subsets:
            if not isDivisibile(divisor,subset): return subset
    return []


if __name__ == '__main__':
    s = [19,10,12,10,24,25,22]
    k = 4
    print(nonDivisibleSubset(k,s))