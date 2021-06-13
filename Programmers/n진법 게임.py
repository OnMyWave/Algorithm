def convert(n,jinsu):
    T = "0123456789ABCDEF"
    div, mod = divmod(n,jinsu)
    if div == 0:
        return T[mod]
    else:
        return convert(div,jinsu) + T[mod]

def solution(n, t, m, p):
    numbers = ""
    i = 0 
    while len(numbers) <= t*m:
        numbers += convert(i,n)
        i += 1

    answer = ""
    for i in range(p-1,len(numbers),m):
        if len(answer) < t:
            answer += numbers[i]
        else:
            break
    return answer