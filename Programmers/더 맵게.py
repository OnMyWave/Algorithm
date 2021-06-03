
### heap 구조가 아닌 일반 list 구조로 해결하려고 했을 때

def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    if scoville[0] == 0 and scoville[1] == 0:
        if K == 0 : 
            return 0
        else:
            return -1
    
    while scoville[0] < K :
        scoville = [scoville[0] + scoville[1]*2] + scoville[2:]
        scoville.sort()
        answer += 1
    return answer

# heap 구조 이용

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try: 
            heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2)) 
        except IndexError: 
            return -1
        answer += 1
    return answer