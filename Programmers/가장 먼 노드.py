def solution(n,edge):
    graph = [[] for _ in range(n) ] # 그래프 만들기
    for e in edge:
        graph[e[0]-1].append(e[1])
        graph[e[1]-1].append(e[0])
    visited = [ 0 for _ in range(n)] # 방문 내역 리스트
    answer = []
    depth = 0

    def DFS(v):
        visited[v-1] = 1
        for node in visited[v-1]:
            count = 0
            if not visited[node-1]:
                DFS(node-1)
                count += 1
            answer.append(count)

    return answer


if __name__ == "__main__":
    print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))