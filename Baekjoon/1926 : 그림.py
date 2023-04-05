from collections import deque

n, m = map(int,input().split())

board = []
visited = [[0] * m for _ in range(n)]

cnt = 0 
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

for _ in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if visited[i][j] or board[i][j] == 0:
            continue

        queue = deque()
        queue.append([i,j])
        visited[i][j] = 1
        cnt = 1
        while queue:
            q = queue.popleft()
            for k in range(4):
                nx = q[0] + dx[k]
                ny = q[1] + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if visited[nx][ny] or board[nx][ny] == 0:
                    continue
                
                cnt += 1
                visited[nx][ny] = cnt
                queue.append([nx,ny])
                

# 전체 제일 넓은 그림 : Max max
# 그림의 개수 : # of 1

cnt_one = 0
cnt_pic = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            cnt_one += 1
        cnt_pic = max(cnt_pic, visited[i][j])

print(cnt_one)
print(cnt_pic)