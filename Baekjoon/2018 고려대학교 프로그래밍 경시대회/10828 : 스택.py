# 명령어
# Push, pop, size, empty, top
import sys

N = int(sys.stdin.readline())
stack = []
cnt = 0
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        stack.append(command[1])
        cnt += 1
    elif command[0] == "top":
        if cnt:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == "size":
        print(cnt)
    elif command[0] == "empty":
        if cnt:
            print(0)
        else:
            print(1)
    else:
        if cnt:
            print(stack.pop())
            cnt -= 1
        else:
            print(-1)
    
