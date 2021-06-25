# DFS

# 1. recursive function

import collections
graph = collections.defaultdict(list)

def recursive_dfs(v,discovered = []):
    discovered.append(v)

    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w,discovered)

    return discovered

# 2. stack

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    
    return discovered

# BFS
# Queue

def iterative_bfs(start_v):
    discovered = []
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

# Backtracking
# 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시
# 후보를 포기 (Backtrack)하여 정답을 찾아가는 범용적인 알고리즘이다.
# DFS가 Backtracking Algorithm의 BackBone
# 백트래킹의 이미지 --> Pruning 