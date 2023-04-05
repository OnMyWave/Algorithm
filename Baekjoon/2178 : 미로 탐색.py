from collections import deque

N, M = map(int,input().split())

board = []

for _ in range(N):
    board.append([int(i) for i in input()])

dx, dy = [-1, +1, 0, 0], [0, 0, -1, +1]
queue = deque()
visited = [[0] * M for _ in range(N)]

# 초기값 설정
queue.append([0,0])
visited[0][0] = 1

cnt = 1
while queue:
    q = queue.popleft()

    for i in range(4):
        nx = q[0] + dx[i]
        ny = q[1] + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M :
            continue
        
        if board[nx][ny] == 0 or visited[nx][ny]:
            continue

        visited[nx][ny] = visited[q[0]][q[1]] + 1
        queue.append([nx,ny])

print(visited[-1][-1])
