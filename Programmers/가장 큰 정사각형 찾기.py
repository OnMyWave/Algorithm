def solution(board):
    cnt = 1
    length = len(board)
    length1 = len(board[0])
    max_area = 0
    
    while cnt <= min(length,length1):
        print(cnt)
        print()
        check = False
        for i in range(length+1-cnt):
            for j in range(length1+1-cnt):
                area = 0 
                for k in range(cnt):
                    for l in range(cnt):
                        area += board[i+k][j+l]
                
                if area == cnt**2:
                    max_area = area
                    check = True
                    break
                    
            if check :
                break
                    
                    
        if max_area != cnt**2:
            break
            
        cnt += 1
        
    return max_area