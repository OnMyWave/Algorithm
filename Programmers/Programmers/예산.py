def solution(d, budget):
    d.sort()
    answer = 0
    for part in d:
        if budget - part >= 0 :
            answer += 1
            budget -= part
            
    return answer