def solution(arr):
    count = 0
    sum = 0
    for number in arr:
        count += 1
        sum += number
    return sum / count