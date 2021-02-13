N, M = map(int, input().split())
graph = []
empty_graph = [[0 for _ in range(M)]] * N
for _ in range(N):
    row = [int(i) for i in input()]
    graph.append(row)

# BFS (1,1) to (-1,-1)

count = 1
bfs_list = []

def BFS(row, column):
    empty_graph[row][column] = 1
    global count
    count += 1
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            try:
                if graph[row + i][column + j]:
                    bfs_list.append([row + i, column + j])
            except:
                pass
    print(bfs_list)
    while empty_graph[N - 1][M - 1] == 0:
        a = bfs_list.pop(0)
        BFS(a[0], a[1])


if __name__ == "__main__":
    BFS(0, 0)
    print(count)
