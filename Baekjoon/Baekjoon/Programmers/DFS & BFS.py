# N, M , V = map(int,input().split())
# graph = [[] for _ in range(N)]
# for _ in range(M):
#     in_node, out_node = map(int,input().split())
#     graph[in_node-1].append(out_node)
#     graph[out_node-1].append(in_node)
#
# for k in graph:
#     k.sort()
#
# d_visited = [False]*N
# def DFS(n):
#     d_visited[n-1] = True
#     print(n,end= ' ')
#     for i in graph[n-1]:
#         if not d_visited[i-1]:
#             DFS(i)
#
# b_visited = [False]*N
# queue = []
# def BFS(n):
#     b_visited[n-1] = True
#     print(n,end= ' ')
#     for i in graph[n-1]:
#         queue.append(i)
#     while queue:
#         b = queue.pop(0)
#         if not b_visited[b-1]:
#             BFS(b)
#
#

N, M, V = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    in_node, out_node = map(int, input().split())
    graph[in_node - 1].append(out_node)
    graph[out_node - 1].append(in_node)

D_visited = [False] * N
dfs_list = []


def DFS(n):
    D_visited[n - 1] = True
    dfs_list.append(n)
    for node in graph[n - 1]:
        if not D_visited[node - 1]:
            DFS(node)


B_visited = [False] * N
bfs_list = []


def BFS(n):
    B_visited[n - 1] = True
    bfs_list.append(n)
    queue = []
    for node in graph[n - 1]:
        queue.append(node)

    while queue:
        a = queue.pop(0)
        if not B_visited[a - 1]:
            BFS(a)



if __name__ == "__main__":
    DFS(V)
    BFS(V)
    print(dfs_list)
    print(bfs_list)
    for v in dfs_list:
        print(v, end=' ')
    print()
    for v in bfs_list:
        print(v, end=' ')
