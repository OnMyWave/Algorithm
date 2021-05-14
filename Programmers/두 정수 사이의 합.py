def solution(a, b):
    count = 0
    if a<=b:
        for num in range(a,b+1):
            count += num
    else:
        for num in range(b,a+1):
            count += num
    return count