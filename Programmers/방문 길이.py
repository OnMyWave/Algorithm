def solution(dirs):
    answer = 0
    current_xy = [0,0]
    visited_edge = []
    cnt = 0 
    
    for dir in dirs : # direction
        temp = current_xy[:] # deep copy
        if dir == 'U':
            current_xy[1] += 1
        elif dir == 'D':
            current_xy[1] -= 1
        elif dir == 'R':
            current_xy[0] += 1
        else:
            current_xy[0] -= 1
        if current_xy[0] < 0 :
            if current_xy[1] < 0 :
                current_xy[0] = max(-5,current_xy[0])
                current_xy[1] = max(-5,current_xy[1])
            else:
                current_xy[0] = max(-5,current_xy[0])
                current_xy[1] = min(5,current_xy[1])
        else:
            if current_xy[1] < 0 :
                current_xy[0] = min(5,current_xy[0])
                current_xy[1] = max(-5,current_xy[1])
            else:
                current_xy[0] = min(5,current_xy[0])
                current_xy[1] = min(5,current_xy[1])
        
        if dir == 'D' or dir == 'L':
            edge = [current_xy[:],temp[:]]
        else:
            edge = [temp[:], current_xy[:]]
        
        if edge not in visited_edge:
            if edge[0] != edge[1]:
                visited_edge.append(edge.copy())
                cnt +=1
        
    return cnt