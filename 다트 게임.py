def solution(dartResult):
    result = [ for s in dartResult if int(s) == True]
    return result

print(solution("1S2D*3T"))