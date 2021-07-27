def solution(stones, k):
    answer = 0
    exist = True
    length = len(stones)
    while True:
        if exist == False :
            break
        i = -1
        while i < length:
            a = 0
            for j in range(k,0,-1):
                try:
                    if stones[i+j]:
                        stones[i+j] -= 1
                        i += j
                        break
                    else:
                        a += 1
                except: 
                    a += 1
        
            if a == k:
                exist = False
                
        answer += 1
    return answer