def solution(n):
    stringOfN = str(n)
    stringOfN = reversed(stringOfN)
    answer = []
    for s in stringOfN:
        answer.append(int(s))
    return answer