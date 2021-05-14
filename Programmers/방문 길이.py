def solution(dirs):
    answer = 0
    current_xy =[0,0]
    visited_edge = []
    cnt = 0 
    
    for dir in dirs : # direction
        x = current_xy[0]
        y = current_xy[1]
        temp = [x,y]
        if dir == 'U':
            current_xy[1] += 1
        elif dir == 'D':
            current_xy[1] -= 1
        elif dir == 'R':
            current_xy[0] += 1
        else:
            current_xy[0] -= 1
        
        edge = sorted([current_xy,temp], key = lambda x: (x[0],x[1]))
        if edge not in visited_edge:
            cnt += 1 
        print(visited_edge)
        print()
        visited_edge.append(edge.copy())
        

            
    return cnt