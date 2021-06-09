def solution(m, n, board):
    board = [list(row) for row in board]
    new_board = list()
    
    while True:
        # 지워지는 2x2 블럭 첫 번째 idx 찾기
        idx = [] 
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != " ":
                    idx.append([i,j])

        # 매치된 블럭 지우기
        for i in idx :
            for j in range(2):
                for k in range(2):
                    board[i[0]+j][i[1]+k] = " "

        # 블록이 지워진 후 아래로 떨어지는 과정
        
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] == " " :
                        board[i+1][j], board[i][j] = board[i][j], " " 
            
        if new_board == board:
                    break
                
        import copy    
        new_board = copy.deepcopy(board)
                
    return sum(x.count(' ') for x in board)
print(solution(	6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))

print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))
print(solution(5,6,["AAAAAA","BBAATB","BBAATB","JJJTAA","JJJTAA"]))
print(solution(6,6,["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE"]))