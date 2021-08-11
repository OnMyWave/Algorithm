import heapq

def solution(N, works):
    heap = []
    for num in works:
        heapq.heappush(heap, [-num, num])

    while N > 0 : 
        p = heapq.heappop(heap)[1]
        if p <= 0: 
            break
        else:
            p -= 1
        heapq.heappush(heap,[-p,p])
        N -= 1
        
    return sum([i[1]**2 for i in heap])