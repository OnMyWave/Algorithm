from collections import deque

M, N = map(int, input().split())

board = []
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    board.append(list(map(int,input().split())))

queue = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            visited[i][j] = 1
            queue.append([i,j])


while queue:
    q = queue.popleft()

    for k in range(4):
        nx = q[0] + dx[k]
        ny = q[1] + dy[k]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if board[nx][ny] == -1 or visited[nx][ny]:
            continue
        
        visited[nx][ny] = visited[q[0]][q[1]] + 1
        queue.append([nx,ny])

all_visited = True
max_days = 0  

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and board[i][j] != -1:
            all_visited = False
        max_days = max(max_days,visited[i][j])

if all_visited:
    print(max_days-1)
else:
    print(-1)

