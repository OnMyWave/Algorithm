N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    in_node, out_node = map(int, input().split())
    graph[in_node - 1].append(out_node)
    graph[out_node - 1].append(in_node)

visited = [False] * N

dfs_list = []

def DFS(n):
	visited[n - 1] = True
	dfs_list.append(n)
	for node in graph[n - 1]:
		if not visited[node - 1]:
			DFS(node)


if __name__ == "__main__":
	DFS(1)
	print(len(dfs_list)-1)
