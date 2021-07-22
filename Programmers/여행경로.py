from collections import defaultdict
def solution(tickets):
    answer = []
    length = len(tickets)
    # maps 생성
    maps = defaultdict(list)
    for i in tickets:
        maps[i[0]].append(i[1])
        
    for i in maps:
        maps[i].sort(reverse = True)
        
    def dfs(v):
        while maps[v]:
            dfs(maps[v].pop())
        answer.append(v)
            
    dfs('ICN') 
    return answer[::-1]