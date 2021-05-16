def solution(A,B):
    answer = 0
    A = sorted(A, reverse = True)
    B = sorted(B)
    cnt = 0
    length = len(A)
    while cnt < length :
        a = A.pop()
        b = B.pop()
        answer += a*b
        cnt += 1

    return answer