def solution(N, stages):
    answer = []
    max_stage = max(stages)
    fail_rate = {}
    for i in range(1,max_stage+1): #현재 스테이지
        a = 0
        b = 0
        for j in stages:
            if j >= i :
                a += 1
            if j == i :
                b += 1
        fail_rate[i] = b/a
    fail_rate = sorted(fail_rate.items(), reverse = True, key = lambda x: x[1] )
    if max_stage > N :
        fail_rate.pop(0)
    for i in range(len(fail_rate)):
        answer.append(fail_rate[i][0])
    return answer