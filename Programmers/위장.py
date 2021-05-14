def solution(clothes):
    clo = {}
    for item in clothes:
        clo[item[1]] = 0
    for item in clothes:
        clo[item[1]] += 1
    if len(clo) == 1:
        return list(clo.values())[0]
    else:
        a = 1
        for value in list(clo.values()):
            a *= (value+1)
        return a - 1