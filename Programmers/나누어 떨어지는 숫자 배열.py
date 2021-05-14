def solution(arr, divisor):
    answer = []
    for component in arr:
        if component % divisor == 0 :
            answer.append(component)
    answer.sort()
    if len(answer) :
        return answer
    else:
        return [-1]