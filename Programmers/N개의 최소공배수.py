def solution(arr):
    lcm = []
    answer = 1
    # 소인수 분해
    for num in arr:
        num_list = []
        div = 2
        while num != 1:
            if num % div == 0:
                num_list.append(div)
                num /= div
                div = 2
            else:
                div += 1
        lcm.append(num_list)

    # 최소공배수 구하기
    for i in lcm:
        while i :
            j = i[0]
            answer *= j
            for k in lcm :
                if j in k:
                    k.remove(j)
    print(lcm)
    return answer

