def solution(s):
    strList = [string for string in s]
    strList = sorted(strList,reverse = True)
    answer = ""
    for s in strList:
        answer += s
    return answer
