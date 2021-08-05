import sys, re
from collections import deque

T = int(input())

for _ in range(T):
    p = [cmd for cmd in input()]
    n = int(input())
    try:
        l = deque(list(map(int,re.sub('[^0-9,]','',input()).split(','))))
    except:
        print('error')
        continue
    i = 0
    e = False
    for cmd in p : 
        if cmd == "R":
            i += 1
        elif cmd == "D":
            if len(l) == 0: 
                e = True
                break
            elif i % 2 :
                l.pop()
            else:
                l.popleft()
    if e :
        print("error")
    else:
        if i % 2 :
            print(list(l)[::-1])
        else:
            print(list(l))

            