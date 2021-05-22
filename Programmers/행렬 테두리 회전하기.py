def solution(rows, columns, queries):
    answer = []
    
    # matrix 정의
    matrix = [[columns * i + j for j in range(1,columns+1)] for i in range(rows)] 
    new_matrix = matrix.copy()
    
    # matrix rotation 시키기
    for rotation in queries:
        changed_number = []
        x1, x2 = rotation[0]-1, rotation[2]-1
        y1, y2 = rotation[1]-1, rotation[3]-1
        dx = x2-x1
        dy = y2-y1
        
        # row 방향
        for i in range(1,dy+1):
            new_matrix[x1][y1+i] = matrix[x1][y1+i-1]
            new_matrix[x2][y2-i] = matrix[x2][y2-i+1]
            changed_number.append(new_matrix[x1][y1+i])
            changed_number.append(new_matrix[x2][y2-i])

        # column 방향
        for j in range(1,dx+1):
            new_matrix[x2-j][y1] = matrix[x2-j+1][y1]
            new_matrix[x1+j][y2] = matrix[x1+j-1][y2]
            changed_number.append(new_matrix[x2-j][y1])
            changed_number.append(new_matrix[x1+j][y2])
            
        print(changed_number)
        answer.append(min(changed_number))
        matrix = new_matrix.copy()
        
    return answer