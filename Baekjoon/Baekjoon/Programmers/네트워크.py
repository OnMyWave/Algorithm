def solution(n,computers):
    answer = 0
    visited = [False] * n
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    def DFS(v):
        visited[v] = True
        for node in graph[v]:
            if not visited[node]:
                DFS(node)


    while False in visited:
        DFS(visited.index(False))
        answer += 1



    return answer


if __name__ == "__main__":
    print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print()
    print()
    print()
    print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
