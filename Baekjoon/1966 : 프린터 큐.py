from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    queue = deque([i for i in enumerate(map(int,input().split()))])
    cnt = 0
 
    while queue :
        a = -1
        for i in queue:
            a = max(a,i[1])
        if queue[0][1] == a :
            p = queue.popleft()
            cnt += 1
            if p[0] == M:
                print(cnt)
                break
        else:
            queue.append(queue.popleft()) 



