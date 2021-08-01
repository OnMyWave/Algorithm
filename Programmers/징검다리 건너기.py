def solution(stones, k):
    answer = 0
    exist = True
    length = len(stones)
    while True:
        i = -1
        while i+k < length:
            a = 0
            for j in range(k,0,-1):
                if stones[i+j]:
                    stones[i+j] -= 1
                    i += j
                    a = 0
                    break
                else:
                    a += 1
            if a == k:
                exist = False

        if exist == False :
            break
        
        answer += 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))