# DFS : 미로에서 길 찾기
# BFS : 수면 위의 파동 느낌

# Graph 그리기
N, M ,V = map(int,input().split())
edge_list = [[]] * N
for _ in range(M):
    s_node , f_node = map(int,input().split())
    edge_list[s_node-1].append(f_node)

# DFS
d_visited = [False]*N
def DFS(node):
    visited[node-1] = True
    print(node,' ',end=' ')
    for i in edge_list[node-1]:
        if not visited[i-1]:
            DFS(i)

# BFS
b_visited = [False]*N

def BFS(node):




if __name__ == "__main__":
    DFS(V)
    BFS(V)