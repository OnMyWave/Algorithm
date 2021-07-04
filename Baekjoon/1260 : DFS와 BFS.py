from collections import defaultdict

N, M, V = map(int,input().split())
maps = defaultdict(list)

for _ in range(M):
    v1, v2 = map(int,input().split())
    maps[v1].append(v2)
    maps[v2].append(v1)

def dfs(v, visited = []):
    visited.append(v)
    for i in maps[v]:
        if i not in visited:
            dfs(i,visited)
    return visited

def bfs(v):
    visited = []
    queue = [v]
    while queue :
        q = queue.pop(0)
        for i in maps[q]:
            if i not in visited:
                visited.append(q)
                queue.append(q)
            
    return visited

print(dfs(V))
print(bfs(V))