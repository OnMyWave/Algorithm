from collections import defaultdict

def solution(id_list, report, k):
    reported = defaultdict(set)
    reporter = defaultdict(set)
    banned_id = []
    answer = []
    for log in report:
        r, d = log.split()

        reported[d].add(r)
        reporter[r].add(d)
        
    for key, value in reported.items():
        if len(value) >= k:
            banned_id.append(key)
    
    for i in id_list:
        cnt = 0 
        for j in reporter[i]:
            if j in banned_id:
                cnt += 1
        answer.append(cnt)
    

    return answer
                