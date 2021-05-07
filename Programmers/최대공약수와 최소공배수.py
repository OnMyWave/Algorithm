
def solution(n, m):
    small = min(n,m)
    gcd = 0
    lcm = 0
    for i in range(1,small+1):
        if n%i == 0 and m%i == 0 :
            gcd = i
    lcm = (n/gcd)*m
    
    return [gcd,lcm]