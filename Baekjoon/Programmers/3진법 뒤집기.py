def convert(n):
    T = "012"
    div, mod = divmod(n,3)
    if div == 0:
        return T[mod]
    else:
        return convert(div) + T[mod]


def solution(n):
    answer = 0
    jinsu_3 = convert(n)
    jinsu_3 = jinsu_3[::-1]
    for i in range(len(jinsu_3)):
        answer+=int(jinsu_3[i])*pow(3,len(jinsu_3)-i-1)

    return answer

print(solution(45))


def solution(n):
    answer = 0
    ternary = []
    while True:
        if n // 3 == 1:
            ternary.extend([n % 3, n // 3])
            break
        ternary.append(n % 3)
        n = n // 3

    ternary.reverse()
    for i in range(len(ternary)):
        answer += pow(3, i) * ternary[i]

    return answer