def solution(board):
    # dp - board 탐색
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] * board[i+1][j] * board[i][j+1] * board[i+1][j+1] :
                board[i+1][j+1] += min(board[i][j], board[i+1][j], board[i][j+1])
    
    # 최댓값 찾기
    find_max = 0
    for i in board:
        find_max = max(max(i),find_max)
    return find_max**2