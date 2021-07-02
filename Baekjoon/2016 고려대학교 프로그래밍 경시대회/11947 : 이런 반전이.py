import sys

def solution(n):
    changed_num = int(''.join(list(map(str,[9-int(i) for i in str(n)]))))
    return changed_num

T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())
    mid = (5*(10**(len(str(num))-1))) #가운데 수 
    if mid > num: #가운데 수와 입력받은 수를 비교 
        print(solution(num)*num)
    else:
        print(mid*(mid-1))
