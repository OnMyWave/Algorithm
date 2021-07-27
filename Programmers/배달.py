def solution(N, road, K):
    answer = []
    maps = [[0 for _ in range(N)] for _ in range(N)]
    for edge in road:
        maps[edge[0]-1][edge[1]-1] = edge[2]
        maps[edge[1]-1][edge[0]-1] = edge[2]
    
    def bfs(v,target):
        cnt = 0
        queue = [v-1]
        visited = [v-1]
        while queue :
            q = queue.pop(0)
            if q == target:
                break
            for i in range(N):
                if i not in visited:
                    if maps[q][i] :
                        queue.append(i)
                        visited.append(i)
                        cnt += maps[q][i]
        return cnt
    print(bfs(1,2))
print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))