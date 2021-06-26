N = int(input())
stairs = []

for _ in range(N):
    stairs.append(int(input()))

dp = [[0,0],[stairs[0],stairs[0]]]

for i in range(2,len(stairs)+1):
    dp.append([max(dp[i-2])+stairs[i-1],stairs[i-1]+dp[i-1][0]])

print(max(dp[-1]))


