# Solution 1. 무지성 침팬지식 bruteforce

from itertools import permutations

def solution(numbers):
    connected_number = []
    numbers = list(permutations(sorted(numbers),len(numbers)))

    for num in numbers:
        connected_number.append(int(''.join([str(i) for i in num])))
    
    return str(max(connected_number))

# Solution 2. 두뇌를 이용하는 사람

def solution(numbers):
    answer = ''
    numbers = sorted([str(number) for number in numbers], key = lambda x : x*3, reverse = True)
    return str(int(''.join(numbers)))