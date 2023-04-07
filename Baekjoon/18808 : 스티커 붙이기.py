from copy import deepcopy 

N, M, K = map(int, input().split())

board = [[0] * M for _ in range(N)]

def rotate(fig):
    
    rotated_fig = [[0]* len(fig) for _ in range(len(fig[0]))]

    for i in range(len(fig)): # Row
        for j in range(len(fig[0])): # column
            rotated_fig[j][i] = fig[len(fig)-i-1][j]

    return rotated_fig


def attach(fig):
    global board
    col = len(fig[0])
    row = len(fig)
    check_break = False    
    for i in range(M - col + 1):
        for j in range(N - row + 1):
            # start_point (i,j)
            temp_board = deepcopy(board)
            check = False # 이미 있는 자리에 그림 찍으려는 경우 체크
            for si in range(col):
                for sj in range(row):
                    if fig[sj][si] and not temp_board[j+sj][i+si] :
                        temp_board[j+sj][i+si] = 1
                    elif fig[sj][si] and temp_board[j+sj][i+si]:
                        check = True
                        break
                if check:
                    break
                
            if not check:
                board = temp_board
                check_break = True # 그림이 삽입된 경우
                break

        if check_break:
            break
    
    return board, check_break

for _ in range(K):
    row, col = map(int, input().split())
    fig = []
    # fig 그리기
    for _ in range(row):
        fig.append(list(map(int,input().split())))

    for i in range(3):
        board, is_attached = attach(fig)
        if is_attached :
            break
        else:
            fig = rotate(fig)
            board, is_attached = attach(fig)

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j]:
            cnt += 1
print(cnt)
