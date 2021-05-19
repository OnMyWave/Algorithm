import numpy as np

def solution(arr):
    arr = np.array(arr)
    small = min(arr)
    gcd = 0
    lcm = 0
    for i in range(1,small+1):
        if arr % i == np.zeros(len(arr)):
            gcd = i
    lcm = small / gcd * max(arr)
    
    return [gcd,lcm]

# print(solution[2,6,8,14])
arr = np.array([2,6,8,14])
arr2 = arr % 2


