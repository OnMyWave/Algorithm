from collections import deque
import sys
deq = deque()
N = int(sys.stdin.readline())
size = 0

for _ in range(N):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push_front' :
        deq.appendleft(int(cmd[1]))
        size += 1
    elif cmd[0] == 'push_back' :
        deq.append(int(cmd[1]))
        size += 1
    elif cmd[0] == 'pop_front':
        if size:
            print(deq.popleft())
            size -= 1
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if size:
            print(deq.pop())
            size -= 1
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(size)
    elif cmd[0] == 'empty':
        if size:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if size:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if size:
            print(deq[-1])
        else:
            print(-1)
        