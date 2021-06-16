import sys

def solution(n):
    changed_num = int(''.join(list(map(str,[9-int(i) for i in str(n)]))))
    return changed_num

T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())
    max_num = -1
    for i in range(1,num+1):
        max_num = max(max_num,i*solution(i))
    
    print(max_num)