def solution(n, lost, reserve):
    answer = n - len(lost)
    lost2 = lost.copy()
    reserve2 = reserve.copy()
    
    for component in lost:
        if component in reserve:
            answer+=1
            reserve2.remove(component)
            lost2.remove(component)
    for component in lost2:
        if component-1 in reserve2:
            answer += 1
            reserve2.remove(component-1)
        elif component+1 in reserve2:
            answer+=1
            reserve2.remove(component+1)
    
    
    return answer