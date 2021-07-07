import heapq
import sys

N = int(sys.stdin.readline())
h = []
for _ in range(N):
    info = int(sys.stdin.readline())
    if info:
        heapq.heappush(h,(abs(info),info))
    else:
        if h :
            print(heapq.heappop(h)[1])
        else:
            print(0)
        
    