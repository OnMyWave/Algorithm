# M, N 입력 받기
M,N = map(int,input().split())

# Board 만들기
board = []
for _ in range(N):
    board.append([i for i in input()])

# board 탐색
for i in range(N-8):
    for j in range(M-8):
        
