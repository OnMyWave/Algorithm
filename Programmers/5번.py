def convert(n):
    T = "01"
    q, r = divmod(n,2)
    if q == 0:
        return T[r]
    else:
        return convert(q) + T[r]

def solution(n):
    answer = 0
    binary_num = convert(n)
    k = 0
    for string in binary_num:
        if string == '1':
            k+=1
    for i in range(0,n-1):
        binary_i = convert(i)
        count = 0
        for j in binary_i:
            if j == '1':
                count+=1
        if count == k:
            answer+=1
    return answer
print(convert(9))
print(solution(9))
