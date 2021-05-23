def solution(n):
    answer = ''
    divisor = 1
    cnt = 0

    while n // divisor :
        divisor *= 3
        cnt += 1
        
    three_list = [3**i for i in range(1,20)] # 11억 6천
    if n in three_list :
        cnt -= 1
    
    for i in range(cnt-1,-1,-1):
    # for i in range(1,cnt+1):
        a = n // (3**i)
        if a == 1:
            answer += "1"
        elif a == 2:
            answer += "2"
        else :
            answer += "4"
        n = n - a*(3**i)
        
    return answer[::-1]
    
def sigma(n):
    sum = 0
    i = 1
    while sum < n:
        sum = sum + 3**i
        i += 1
    return i-1

print(sigma(13))