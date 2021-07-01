from collections import deque

m = [i for i in input()]
N = int(input())
words = []

for _ in range(N):
    w, g = input().split()
    queue = deque(m)
    for i in w : 
        try:
            if queue[0] == i:
                queue.popleft()
        except:
            pass

    if len(queue) == 0 :
        words.append([w,int(g)/(len(w)-len(m))])

if len(words) == 0 :
    print("No Jam")
else:
    words.sort(key = lambda x: -x[1])
    print(words[0][0])