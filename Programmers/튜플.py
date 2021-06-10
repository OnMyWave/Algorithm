def solution(s):
    
    # Bracket 단위 indexing
    idx = []
    open_bracket = -1
    for i in range(1,len(s)-1):
        if s[i] == "{":
            open_bracket = i
        elif s[i] == "}":
            idx.append([open_bracket,i])
            open_bracket = -1
            
    # Bracket 단위에서 (,) 단위 component 분리
    numbers = []
    
    for i in idx :
        numbers.append(s[i[0]+1:i[1]].split(','))
            

    # len 기준 정렬
    numbers.sort(key=len)
    
    # set operation을 통해 tuple 분리
    answer = [numbers[0][0]]
    for i in range(1,len(numbers)):
        answer.append(list(set(numbers[i])-set(numbers[i-1]))[0])

    # 답 도출
    return list(map(int,answer))