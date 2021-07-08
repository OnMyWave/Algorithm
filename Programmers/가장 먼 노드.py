from collections import deque, defaultdict

def solution(n, edge):

    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    def BFS(v):
        queue = deque([v])
        visited = [0,1] + [0] * (n-1)
        while queue :
            q = queue.popleft()
            for i in graph[q]:
                if visited[i] == 0:
                    visited[i] = visited[q] + 1
                    queue.append(i)
        return visited.count(max(visited))

    return BFS(1)

if __name__ == "__main__":
    print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))