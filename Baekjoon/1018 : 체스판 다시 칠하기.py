# M, N 입력 받기
M,N = map(int,input().split())

# Board 만들기
board = []
for _ in range(N):
    board.append([i for i in input()])

# Board Type
type1 = [["W","B","W","B","W","B","W","B"] if i%2 else ["B","W","B","W","B","W","B","W"] for i in range(8) ] # W가 먼저

type2 = [["W","B","W","B","W","B","W","B"] if i%2 else ["W","B","W","B","W","B","W","B"]for i in range(8) ]  # B가 먼저

import sys
# board 탐색
min_cnt = sys.maxsize
for i in range(N-8):
    for j in range(M-8):
        error1 = 0
        error2 = 0 
        for k in range(8):
            for l in range(8):
                if board[i+k][j+l] != type1[k][l]:
                   error1 += 1
                if board[i+k][j+l] != type2[k][l]:
                   error2 += 1
        min_cnt = min(error1,error2,min_cnt)

print(min_cnt)

