N, M = map(int,input().split())
basket = []
max_x, max_y = -1, -1
for _ in range(N):
    x,y = map(int,input().split())
    basket.append([x,y])
    max_x = max(max_x,x) 
    max_y = max(max_y,y)
    # x,y 최댓값

# map 만들기
maps = [[0 for _ in range(max_y+1)] for _ in range(max_x+1)]
for i in basket:
    maps[i[0]][i[1]] = M - (i[0]+i[1])

# dp
for i in range(1,max_x+1):
    for j in range(1,max_y+1):
        maps[i][j] += max(maps[i][j-1],maps[i-1][j])

# 캔디 최댓값 찾기
candy = -1
for i in maps:
    for j in i:
        candy = max(candy,j)
print(candy)
