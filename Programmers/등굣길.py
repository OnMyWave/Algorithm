def solution(m, n, puddles):
    puddles = set([(y-1, x-1) for x, y in puddles])
    dist = [[0] * (m) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dist[i][j] = 1
            else:
                dist[i][j] = 0 if (i, j) in puddles else dist[i-1][j] + dist[i][j-1]

                
    return dist[n-1][m-1] % 1000000007