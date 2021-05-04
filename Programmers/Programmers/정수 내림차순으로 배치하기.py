def solution(n):
    answer = ""
    numList = [s for s in str(n)]
    numList = sorted(numList,reverse=True)
    for s in numList:
        answer += s
    return int(answer)