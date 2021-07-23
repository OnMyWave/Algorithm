# 처음 생각 -> but factorial로 인해 o(n!)
from itertools import permutations

def solution1(n, k):
    return list(permutations([i for i in range(1,n+1)],n))[k-1]
