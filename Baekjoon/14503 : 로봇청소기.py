from collections import deque

N, M = map(int,input().split()) # N X M maps

# r,c : 로봇청소기 위치
# d : 로봇청소기의 방향 {
# 북 동 남 서 순
# }
r, c, d = map(int,input().split()) 

# 0: 청소 x
# 1: 벽
board = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

queue = deque()

queue.append([r,c,d])

board[r][c] = 2

cnt = 0
while queue :
    q = queue.popleft()

    for i in range(4):
        next_dir = (q[2] + 3 - i)%4
        nx = q[0] + dx[next_dir]
        ny = q[1] + dy[next_dir]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny]:
            continue

        board[nx][ny] = 2
        queue.append([nx,ny,next_dir])
        break

    if not queue:
        
        nx = q[0] + dx[(q[2]+2)%4]
        ny = q[1] + dy[(q[2]+2)%4]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == 1:
            continue

        
        queue.append([nx,ny,q[2]])


for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            cnt += 1


print(cnt)





         





