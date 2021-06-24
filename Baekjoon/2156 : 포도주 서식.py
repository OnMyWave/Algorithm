N = int(input())
wine = []

for _ in range(N):
    wine.append(int(input()))

if len(wine) <= 2 :
    print(sum(wine))
else:
    dp = [[0,0],[wine[0],wine[0]]]

    for i in range(2,len(wine)+1):
        dp.append([max(dp[i-2])+wine[i-1],wine[i-1]+dp[i-1][0],max(dp[i-1])])

    print(dp)



