def solution(citations):
    answer = -1
    max_cit = max(citations)
    for i in range(max_cit):
        count = 0
        for citation in citations:
            if citation >= i :
                count += 1
        if count < i :
            break
        answer += 1
    if max_cit == 0:
        return 0
    return answer