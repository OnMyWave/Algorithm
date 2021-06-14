def solution(N, stages):
    # 기본 자료형 정의
    answer = []
    max_stage = max(stages)
    fail_rate = {}

    # Stage별 실패율 구하기
    for i in range(1,max_stage+1): #현재 스테이지
        a = 0
        b = 0
        for j in stages:
            if j >= i :
                a += 1
            if j == i :
                b += 1
        fail_rate[i] = b/a
    
    # 도달하지 못한 Stage 실패율 정의
    for i in range(1,N+1):
        if i not in fail_rate:
            fail_rate[i] = 0

    # 실패율이 높은 순으로 정렬        
    fail_rate = sorted(fail_rate.items(), reverse = True, key = lambda x: x[1] )

    # 스테이지 하나 추가되는 것 제거
    if max_stage > N :
        fail_rate.pop(0)
    
    for i in range(len(fail_rate)):
        answer.append(fail_rate[i][0])
    return answer