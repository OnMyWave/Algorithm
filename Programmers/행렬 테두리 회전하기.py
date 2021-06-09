import sys

def solution(rows, columns, queries):
    answer = []
    
    # matrix 정의
    matrix = [[columns * i + j for j in range(1,columns+1)] for i in range(rows)] 
    copyed_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    
    # matrix rotation 시키기
    for rotation in queries:
        minimum = sys.maxsize

        x1 = rotation[0]-1
        x2 = rotation[2]-1
        y1 = rotation[1]-1
        y2 = rotation[3]-1
        dx = x2-x1
        dy = y2-y1
        # copyed_matrix 값 복사
        for i in range(dy):
            copyed_matrix[x1][y1+i] = matrix[x1][y1+i]
            copyed_matrix[x2][y2-i] = matrix[x2][y2-i]
            

        # column 방향
        for j in range(dx):
            copyed_matrix[x2-j][y1] = matrix[x2-j][y1]
            copyed_matrix[x1+j][y2] = matrix[x1+j][y2]
    

        # row 방향
        for i in range(1,dy+1):
            matrix[x1][y1+i] = copyed_matrix[x1][y1+i-1]
            matrix[x2][y2-i] = copyed_matrix[x2][y2-i+1]
            minimum = min(matrix[x1][y1+i],matrix[x2][y2-i],minimum)

        # column 방향
        for j in range(1,dx+1):
            matrix[x2-j][y1] = copyed_matrix[x2-j+1][y1]
            matrix[x1+j][y2] = copyed_matrix[x1+j-1][y2]
            minimum = min(matrix[x2-j][y1],matrix[x1+j][y2],minimum)
            
        answer.append(minimum)
        
    return answer