from itertools import combinations

def checkingPrimeNumber(n):
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True

def solution(nums):
    sumOfCombination = [i+j+k for i,j,k in combinations(nums,3)]
    answer = 0
    for component in sumOfCombination:
        if checkingPrimeNumber(component):
            answer +=1
    return answer