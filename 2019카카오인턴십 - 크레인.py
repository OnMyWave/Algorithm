def solution(board, moves):
    answer = 0
    N = len(board)
    blanket = []
    # N*N Board
    for column in moves:
        for row in range(N):
            if board[row][column - 1] != 0:
                blanket.append(board[row][column - 1])
                board[row][column - 1] = 0
                break

    for _ in range(len(blanket)):
        for i in range(0, len(blanket) - 1):
            if blanket[i] == blanket[i + 1]:
                blanket[i] = 0
                blanket[i + 1] = 0
                for _ in range(2):
                    blanket.remove(0)
                answer += 2
                break
    return answer
