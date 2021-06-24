import sys

N = int(sys.stdin.readline())
houses = []

for _ in range(N):
    houses.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,N):
    for j in range(3):
        if j == 2:
            houses[i][j] += min(houses[i-1][j-1],houses[i-1][0])
        else:
            houses[i][j] += min(houses[i-1][j-1],houses[i-1][j+1])

print(min(houses[-1]))