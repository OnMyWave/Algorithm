def solution(arr):
    answer = []
    length = len(arr)
    i = 0 
    while i<length-1:
        if arr[i] == arr[i+1]:
            arr[i] = -1 
        i+=1
    for number in arr:
        if number != -1:
            answer.append(number)
    return answer