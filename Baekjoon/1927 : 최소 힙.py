import heapq
import sys

N = int(sys.stdin.readline())
h = []
for _ in range(N):
    info = int(sys.stdin.readline())
    if info:
        heapq.heappush(h,info)
    else:
        if h :
            print(heapq.heappop(h))
        else:
            print(0)
        
    