from collections import defaultdict

def solution(n):
    fib = defaultdict(int)
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n] % 1234567