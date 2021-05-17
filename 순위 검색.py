def solution(info, query):
    answer = []
    # Query 분리 작업 1 : 기본
    info_data = [[j for j in info[i].split(" ")] for i in range(len(info))]
    query_data = [[j for j in query[i].split(" and ")] for i in range(len(query))]
    
    # Query 분리 작업 2 : 점수 분리
    length = len(query)
    for i in range(length):
        query_data[i] += query_data[i].pop().split()

    # info_data 정렬
    info_data = sorted(info_data, key = lambda x: x[0])
    
    # Query 검색
    for q in query_data:
        cnt = 0 
        language = q[0]
        apply = q[1]
        career = q[2]
        soulFood = q[3]
        score = q[4]
        for person in info_data:
            if person[0] == language or language == '-':
                if person[1] == apply or apply == '-':
                    if person[2] == career or career == '-':        
                        if person[3] == soulFood or soulFood == '-':
                            if score == '-' or int(person[4]) >= int(score) :
                                cnt+=1
                
        answer.append(cnt)
    print(info_data)
    return answer



print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))